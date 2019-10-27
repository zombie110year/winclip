"""clip2tex

监听并获取 windows 剪贴板中的文本，使用 latex 编译后将结果转化为 bitmap 复制到剪贴板中。
方便制作 latex 公式图片。
"""

from win32.win32clipboard import *

from .clipboard import ClipBoard

__author__ = "zombie110year <zombie110year@outlook.com>"
__version__ = '0.1.0'
