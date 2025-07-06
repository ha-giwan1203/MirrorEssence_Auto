# MirrorEssence_Auto

📊 GPT 기반 판단 시스템 MirrorEssence의 자동화 운영 버전입니다.  
Slack 업로드, Notion 카드 생성, 회람 리포트 PDF 자동 생성까지 하나의 흐름으로 통합되어 있습니다.

---

## ✅ 주요 기능

- 🔗 PDF 파일 Slack 채널 전송 (files_upload_v2)
- 🧾 Notion DB 카드 자동 생성 (필드 점검 포함)
- 📄 실행 로그 저장 (`mirror_history.json`)
- 📑 회람 리포트 PDF 자동 생성
- 🖥️ Streamlit UI 제공

---

## 📁 폴더 구조

```
├── config/
│   ├── notion_fields.json
│   └── judgment_rules.json
├── outputs/
│   └── mirror_execution_summary_2025-07-06.pdf
├── .env.example
├── .gitignore
├── upload_final_report.py
```

---

## ⚙️ 설치 방법

```bash
pip install -r requirements.txt
```

---

## 🚀 실행 방법

### 1. Streamlit UI

```bash
streamlit run streamlit_ui_runner.py
```

### 2. PDF 회람 리포트 수동 전송

```bash
python upload_final_report.py
```

---

## 🔐 주의사항

`.env` 파일은 포함되어 있지 않습니다.  
아래 항목을 `.env` 파일에 직접 설정해주세요:

```env
SLACK_BOT_TOKEN=...
SLACK_CHANNEL=...
GDRIVE_FOLDER_ID=...
NOTION_TOKEN=...
NOTION_DATABASE_ID=...
```

---

## 📦 제작자

지완 (ha-giwan1203)  
시스템 설계, 자동화 구성, 실전 운영 완료 💙
