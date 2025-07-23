
import json
import os
from datetime import datetime

log_dir = "logs"
output_file = os.path.join(log_dir, "evaluation_aggregated_log.jsonl")

def read_json_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def aggregate_logs():
    aggregated = []

    # Load rag feedback loop logs
    rag_path = os.path.join(log_dir, "loop_evaluation_log.json")
    if os.path.exists(rag_path):
        rag_logs = read_json_lines(rag_path)
        for entry in rag_logs:
            aggregated.append({
                "type": "RAG_FEEDBACK",
                "memory": entry.get("memory"),
                "score": entry.get("evaluation", {}).get("score"),
                "reason": entry.get("evaluation", {}).get("reason"),
                "timestamp": entry.get("timestamp")
            })

    # Load CoT logs
    cot_path = os.path.join(log_dir, "cot_prompt_test_log.json")
    if os.path.exists(cot_path):
        with open(cot_path, "r", encoding="utf-8") as f:
            cot_entry = json.load(f)
            aggregated.append({
                "type": "COT_PROMPT",
                "memory": cot_entry.get("memory"),
                "cot_prompt": cot_entry.get("cot_prompt"),
                "timestamp": cot_entry.get("timestamp")
            })

    # Write output
    with open(output_file, "w", encoding="utf-8") as f:
        for item in aggregated:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"✅ 통합 로그 저장 완료 → {output_file}")

if __name__ == "__main__":
    aggregate_logs()
