import os
import subprocess

if __name__ == "__main__":
    # NOTE: Windowsではパス区切りが \ のため問題となる可能性がありjoinを使う
    path = f"{os.path.dirname(__file__)}/src/path.py"
    subprocess.run(["python", path])