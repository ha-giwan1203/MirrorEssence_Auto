import os
from datetime import datetime
from dotenv import load_dotenv
from slack_sdk import WebClient

# 환경 변수 불러오기
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

client = WebClient(token=SLACK_BOT_TOKEN)

# 리포트 파일명
today = datetime.now().strftime("%Y-%m-%d")
report_path = f"mirror_execution_summary_{today}.pdf"

# Slack 업로드 실행
if os.path.exists(report_path):
    with open(report_path, "rb") as f:
        response = client.files_upload_v2(
            file=f,
            filename=os.path.basename(report_path),
            title="Mirror 실행 회람 리포트",
            channels=[SLACK_CHANNEL],
            initial_comment="📎 자동 생성된 회람 리포트를 공유합니다."
        )
        print("✅ 업로드 성공:", response["file"]["permalink"])
else:
    print("❌ 리포트 파일을 찾을 수 없습니다:", report_path)
