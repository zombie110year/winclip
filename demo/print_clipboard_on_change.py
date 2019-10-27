"""Show Clipboard

while clipboard changed, show its content in console
"""

from clip2tex.clipboard import ClipBoard
from time import strftime
from time import localtime


def show_clipboard():
    timestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())
    content = ClipBoard.read()
    print(f"[{timestamp}] {content}")


if __name__ == "__main__":
    ClipBoard.listen(show_clipboard)
