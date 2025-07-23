import os
import subprocess
import shutil

def cleanup_tmp_driveupload():
    folder_path = ".tmp.driveupload"
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print("[정리 완료] .tmp.driveupload 폴더 삭제 완료")
        except Exception as e:
            print(f"[정리 실패] {e}")

def sync_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "자동 백업: 최신 상태 동기화"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("[✅] GitHub 동기화 완료")
    except subprocess.CalledProcessError as e:
        print(f"[❌] Git 명령 실패: {e}")
    except Exception as e:
        print(f"[❌] 기타 오류: {e}")

if __name__ == "__main__":
    print("[시작] .tmp.driveupload 정리 및 GitHub 자동 동기화")
    cleanup_tmp_driveupload()
    sync_to_github()
