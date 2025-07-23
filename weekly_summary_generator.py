
from pathlib import Path
from datetime import datetime
import json

log_path = Path("logs/evaluation_aggregated_log.jsonl")
summary_path = Path("reflection_md")
summary_path.mkdir(exist_ok=True)

if not log_path.exists():
    print("❌ 통합 로그 파일이 없습니다.")
    exit()

today = datetime.today()
year, week = today.isocalendar()[0:2]
filename = f"weekly_summary_{year}W{week:02}.md"
output_path = summary_path / filename

with open(log_path, encoding="utf-8") as f:
    lines = f.readlines()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"# GIWANOS 주간 요약 보고서 ({year}년 {week}주차)\n\n")
    f.write(f"- 생성일: {today.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"- 총 평가 기록 수: {len(lines)}\n\n")
    for i, line in enumerate(lines, 1):
        entry = json.loads(line)
        f.write(f"---\n### 기록 {i}\n")
        f.write(f"- 타입: {entry.get('type')}\n")
        f.write(f"- 기억: {entry.get('memory')}\n")
        if entry.get("score"):
            f.write(f"- 점수: {entry.get('score')} ({entry.get('reason')})\n")
        if entry.get("cot_prompt"):
            f.write("- CoT:\n\n")
            f.write("```\n")
            f.write(entry.get("cot_prompt"))
            f.write("\n```\n")
        f.write(f"- 시각: {entry.get('timestamp')}\n\n")

print(f"✅ 주간 요약 보고서 생성 완료 → {output_path}")
