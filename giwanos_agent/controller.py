# controller.py - 에이전트 운영체 자동 실행기

from giwanos.judge.judge_agent import JudgeAgent
import sys

def main():
    if len(sys.argv) < 2:
        print("❗ 실행 모드를 지정해주세요 (예: reflection, evaluation, report, snapshot, self_check, auto)")
        return

    mode = sys.argv[1]
    user_prompt = sys.argv[2] if len(sys.argv) > 2 else ""

    agent = JudgeAgent()

    if mode == "auto":
        print("[Controller] 🤖 자동 실행 시작 (플래너 기반)")
        result = agent.run_plan_and_execute(user_prompt)
    else:
        result = agent.run_loop(mode)

    print("[Controller] 실행 결과:")
    print(result)

if __name__ == "__main__":
    main()
