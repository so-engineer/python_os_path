import os
import subprocess

if __name__ == "__main__":
    # NOTE: Windowsではパス区切りが \ となり問題となる可能性があるためjoinを使う
    # path = f"{os.path.dirname(__file__)}/src/path.py"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "path.py")
    subprocess.run(["python", path])