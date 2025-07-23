<<<<<<< HEAD
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)


from fpdf import FPDF
import os

FONT_PATH = os.path.join(os.getcwd(), "Nanum_Gothic", "NanumGothic-Regular.ttf")

pdf = FPDF()
pdf.add_page()
pdf.add_font("Nanum", "", FONT_PATH)
pdf.set_font("Nanum", size=12)

lines = [
    "🧠 GIWANOS 회고 PDF 테스트입니다.",
    "한글이 정상 출력되어야 합니다.",
    "이 파일은 자동으로 NanumGothic 폰트를 사용합니다."
]

for line in lines:
    safe_line = line.replace("\n", " ").strip()
    pdf.cell(0, 10, txt=safe_line, ln=True)

output_path = "loop_reflection_log.pdf"
pdf.output(output_path)
print(f"✅ 회고 PDF 생성 완료: {output_path}")
=======

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
import json
from datetime import datetime
import textwrap

log_path = Path("logs/evaluation_aggregated_log.jsonl")
font_path = Path(__file__).parent / "Nanum_Gothic" / "NanumGothic-Regular.ttf"
report_path = Path("reports")
report_path.mkdir(exist_ok=True)

if not log_path.exists():
    print("❌ 평가 로그 파일이 없습니다.")
    exit()

if not font_path.exists():
    print("❌ 폰트 파일이 없습니다.")
    exit()

pdf_file = report_path / f"evaluation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
c = canvas.Canvas(str(pdf_file), pagesize=A4)
width, height = A4

# Register Korean font
pdfmetrics.registerFont(TTFont("Nanum", str(font_path)))
c.setFont("Nanum", 12)

y = height - 50
c.drawString(200, y, "GIWANOS 평가 보고서")
y -= 30
c.setFont("Nanum", 10)

def draw_wrapped(label, value, y):
    lines = textwrap.wrap(value or "", width=90)
    c.drawString(50, y, f"{label}")
    y -= 15
    for l in lines:
        c.drawString(60, y, l)
        y -= 15
    return y

with open(log_path, encoding="utf-8") as f:
    for line in f:
        if y < 100:
            c.showPage()
            c.setFont("Nanum", 10)
            y = height - 50

        entry = json.loads(line)
        y = draw_wrapped("[TYPE]", entry.get("type", ""), y)
        y = draw_wrapped("[MEMORY]", entry.get("memory", ""), y)
        if entry.get("score"):
            y = draw_wrapped("[SCORE]", f"{entry['score']} ({entry.get('reason', '')})", y)
        if entry.get("cot_prompt"):
            y = draw_wrapped("[COT]", entry["cot_prompt"], y)
        y = draw_wrapped("[TIME]", entry.get("timestamp", ""), y)
        y -= 10

c.save()
print(f"✅ PDF 보고서 생성 완료 → {pdf_file}")
>>>>>>> 61149de (🎯 Git 초기화 및 복구 완료)
