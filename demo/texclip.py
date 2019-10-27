"""当复制新内容时，将内容编译为 standalone 文档并转化为 png 格式保存在当前目录

.. code:: sh

    python -m demo.texclip

复制文件末端的内容，体验效果

你需要安装有 texlive、imagemagick 以及 ghostscript 并确保
xelatex, magick, gs 程序位于 PATH 环境变量规定的目录中。

可能需要提前修改 magick 的 delegate.xml 配置，将 ``&quot;@PSDelegate@&quot;`` 修改为 ``gs``
以规避 ``gswin32c`` 不存在的问题。
"""
from pathlib import Path
from subprocess import PIPE
from subprocess import CalledProcessError
from subprocess import TimeoutExpired
from subprocess import run
from tempfile import TemporaryDirectory
from tempfile import gettempdir
from time import localtime
from time import strftime

from win10toast import ToastNotifier
from winclip import *


def now() -> str:
    "返回当前时间戳"
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


def tex_content(text: str) -> str:
    return ("\\documentclass[preview]{standalone}\n"
            "\\usepackage{amsmath}\n"
            "\\usepackage{amssymb}\n"
            "\\begin{document}\n"
            f"{text}\n"
            "\\end{document}\n")


def main():
    print(f"\x1b[33m[{now()}]\x1b[0m")
    base = Path(gettempdir()) / "texclip"
    text = ClipBoard.read(CF_UNICODETEXT)
    with TemporaryDirectory() as workspace:
        workspace = Path(workspace)
        template = tex_content(text)

        texfile = workspace / "main.tex"
        texfile.write_bytes(template.encode("utf-8"))
        tex_cmd = ["xelatex", texfile.as_posix()]
        try:
            tex_status = run(tex_cmd, shell=False, cwd=workspace,
                             stdout=PIPE, stderr=PIPE, timeout=10)
            tex_status.check_returncode()
        except TimeoutExpired as e:
            print(f"error in tex: {text}")
            print("\x1b[31m")
            print(e.stdout.decode("utf-8"))
            print("\x1b[0m")
            return
        except CalledProcessError as e:
            print(f"error in tex: {text}")
            print("\x1b[31m")
            print(e.stderr.decode("utf-8"))
            print("\x1b[0m")
            return

        # main.pdf 已生成
        pdffile = workspace / "main.pdf"
        outimgfile = base / \
            f"texclip-{strftime('%Y%m%d-%H%M%S', localtime())}.png"
        magick_cmd = ["magick", "-density", "300",
                      pdffile.as_posix(), "-quality", "100",
                      "-trim", outimgfile.absolute().as_posix()]
        try:
            magick_status = run(magick_cmd, shell=False, cwd=workspace,
                                stdout=PIPE, stderr=PIPE, timeout=5)
            magick_status.check_returncode()
        except TimeoutExpired as e:
            print(f"[{now()}] error in magick")
            print("\x1b[31m")
            print(e.stdout.decode("utf-8"))
            print("\x1b[0m")
            return
        except CalledProcessError as e:
            print(f"[{now()}] error in magick")
            print("\x1b[31m")
            print(e.stderr.decode("utf-8"))
            print("\x1b[0m")
            return

        print(f"\x1b[32m{text[:10]}.. saved at {outimgfile.as_posix()}\x1b[0m")
        ToastNotifier().show_toast("Task Completed",
                                   f"{outimgfile.absolute().as_posix()}")


if __name__ == "__main__":
    base = Path(gettempdir()) / "texclip"
    if not base.exists():
        base.mkdir()

    while True:
        try:
            ClipBoard.listen(main)
        except KeyboardInterrupt:
            break
        except:
            continue

r"""

Hello, \LaTeX, Let's Show a Math euqation:

inline math: $E = mc^2$ and display math:

$$
\sum_{i=0}^{N} i = \frac{n (n+1)}{2}
$$

Sorry, dont support CJK fonts, If you want, edit the template above.

"""
