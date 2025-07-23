<<<<<<< HEAD
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)

import json
from pathlib import Path

base_path = Path(__file__).resolve().parent
state_file = base_path / "loop_memory_state.json"
log_file = base_path / "loop_result_log.json"

def show_state():
    print("\n🧠 [GIWANOS 상태 요약]")
    if state_file.exists():
        state = json.loads(state_file.read_text(encoding="utf-8"))
        for k, v in state.items():
            print(f"{k}: {v}")
    else:
        print("loop_memory_state.json 없음")

def show_log():
    print("\n📋 [루프 실행 결과 로그]")
    if log_file.exists():
        logs = json.loads(log_file.read_text(encoding="utf-8"))
        for entry in logs.get("results", [])[-5:]:
            print(f"- [{entry.get('timestamp')}] {entry.get('loop')} ▶ {entry.get('status')}")

if __name__ == "__main__":
    show_state()
    show_log()
=======
import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GIWANOS 대시보드", layout="wide")
st.title("📊 GIWANOS 상태 대시보드")

def show_summary():
    summary_path = Path("giwanos_status_summary.json")
    if not summary_path.exists():
        st.warning("상태 요약 파일이 없습니다.")
        return

    with open(summary_path, encoding="utf-8") as f:
        data = json.load(f)

    st.subheader("🧠 [GIWANOS 상태 요약]")
    for key, value in data.items():
        st.write(f"**{key}**: {value}")

def show_log():
    log_dir = Path("agent_logs")
    if not log_dir.exists():
        st.warning("agent_logs 폴더가 없습니다.")
        return

    log_files = sorted(log_dir.glob("agent_log_*.json"))
    if not log_files:
        st.warning("에이전트 로그 파일이 없습니다.")
        return

    latest_log = log_files[-1]
    st.subheader("📋 [에이전트 실행 로그]")

    try:
        logs = json.loads(latest_log.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # fallback for JSONL-like formats
        logs = [json.loads(line) for line in latest_log.read_text(encoding="utf-8").splitlines() if line.strip()]

    for log in logs:
        st.json(log)

show_summary()
show_log()
>>>>>>> 61149de (🎯 Git 초기화 및 복구 완료)
