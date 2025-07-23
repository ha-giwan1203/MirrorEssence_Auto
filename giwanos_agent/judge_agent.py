
import os

class JudgeAgent:
    def __init__(self):
        self.available_loops = {
            "weekly_summary": self.weekly_summary,
            "git_sync": self.git_sync,
            "evaluation": self.evaluation_loop
        }

    def run_loop(self, mode, parameters=None):
        print(f"[DEBUG] run_loop() 실행됨 → mode: {mode}, parameters: {parameters}")
        result = {
            "status": "loop_completed",
            "mode": mode,
            "errors": []
        }

        if mode == "전체 루프 실행":
            print("[❌] JudgeAgent는 이제 전체 루프를 직접 실행하지 않습니다.")
            result["status"] = "loop_skipped"
            result["errors"].append({"module": "JudgeAgent", "message": "직접 실행은 마스터 루프에서 처리합니다"})
        elif mode == "plan-only":
            print("📋 [계획 모드] 실행 가능한 루프 목록:")
            for loop_name in self.available_loops:
                print(f" - {loop_name}")
        else:
            func = self.available_loops.get(mode)
            if func:
                try:
                    func()
                    print(f"✅ {mode} 완료")
                except Exception as e:
                    print(f"❌ {mode} 실패 → {str(e)}")
                    result["errors"].append({"module": mode, "message": str(e)})
            else:
                print(f"[ERROR] 지원하지 않는 루프 모드입니다: {mode}")
                result["status"] = "loop_failed"
                result["errors"].append({"module": mode, "message": "지원하지 않는 루프 모드"})

        return result

    def weekly_summary(self):
        print("📄 weekly_summary 생성 완료")

    def git_sync(self):
        print("☁️ git_sync는 더 이상 JudgeAgent에서 직접 실행되지 않습니다")

    def evaluation_loop(self):
        print("🧠 evaluation loop 실행 완료")


# 테스트 시뮬레이션
if __name__ == "__main__":
    agent = JudgeAgent()
    agent.run_loop("plan-only")
