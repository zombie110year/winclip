"""clip2tex

监听并获取 windows 剪贴板中的文本，使用 latex 编译后将结果转化为 bitmap 复制到剪贴板中。
方便制作 latex 公式图片。
"""

from .clipboard import ClipBoard
from .extern_call import ImageMagick
from .extern_call import XeLaTeX

__all__ = ("ClipBoard", "ImageMagick", "XeLaTeX")
__author__ = "zombie110year <zombie110year@outlook.com>"
__version__ = '0.1.0'
