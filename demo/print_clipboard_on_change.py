"""Show Clipboard

while clipboard changed, show its content in console
"""


from time import localtime
from time import strftime

from winclip import *


def show_clipboard():
    timestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())
    content = ClipBoard.read()
    print(f"[{timestamp}] {content}")


if __name__ == "__main__":
    ClipBoard.listen(show_clipboard)
