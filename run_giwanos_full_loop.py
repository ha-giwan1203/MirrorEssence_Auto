import subprocess
import os

subprocess.run(["python", "run_codex_auto.py"], check=True)
import os
import subprocess

print("🔁 GIWANOS 회고 루프 통합 실행 시작")

# Step 1: 회고 평가 루프
print("▶️ rag_feedback_loop.py 실행")
subprocess.run(["python", "advanced_modules/rag_feedback_loop.py"], check=True)

# Step 2: CoT 생성기 실행
print("▶️ test_cot_prompt.py 실행")
subprocess.run(["python", "advanced_modules/test_cot_prompt.py"], check=True)

# Step 3: 재랭킹 평가기 실행
print("▶️ test_re_ranker.py 실행")
subprocess.run(["python", "advanced_modules/test_re_ranker.py"], check=True)

# Step 4: 평가 통합기 실행
print("▶️ aggregate_evaluation_logs.py 실행")
subprocess.run(["python", "aggregate_evaluation_logs.py"], check=True)

print("\n✅ GIWANOS 통합 루프 완료 → 평가 데이터 통합됨")

# Step 5: 이메일 보고 전송
print("▶️ send_evaluation_report.py 실행")
subprocess.run(["python", "send_evaluation_report.py"], check=True)

# Step 6: GitHub 백업 업로드
print("▶️ git_sync.py 실행")
subprocess.run(["python", "git_sync.py"], check=True)

# Step 7: 주간 요약 마크다운 생성
print("▶️ weekly_summary_generator.py 실행")
subprocess.run(["python", "weekly_summary_generator.py"], check=True)
