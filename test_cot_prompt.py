import os
import sys
from giwanos.judge.cot_prompt import generate_cot_prompt

# 패키지 경로 등록
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

# Sample reflection
reflection = "이번 주에는 코드 리뷰 자동화 도구를 도입하여 효율을 높였습니다."

prompt = generate_cot_prompt(reflection)
print(prompt)