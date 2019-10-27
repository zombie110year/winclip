"""剪贴板
======

1. 监听剪贴板变动
2. 读写剪贴板

Clipboard
=========

1. watch clipboard updating
2. read/write clipboard
"""
import win32.win32clipboard as wc
from time import sleep

__all__ = ("ClipBoard")


class ClipBoard:
    """Windows ClipBoard

    Support ``read/write`` and ``listen``.

    Example
    =======

    You can specify which format to read

    >>> ClipBoard.read(win32.win32clipboard.CF_UNICODETEXT)
    "Hello World"

    or auto detect the first format of ``EnumClipboardFormats()``
    If you copied a text, the default format is ``CF_OEMTEXT``
    (``bytes`` in python)

    >>> ClipBoard.read()
    b"Hello World"

    If You want to copy a image, should be a BitMap, and read/write it as a ``CF_DIB``
    (Device Independent Bitmap)

    >>> ClipBoard.write(b"BM...")

    You can listen clipboard change event by ``listen(lambda : ...)``, default interval is 0.1 s.

    >>> ClipBoard.listen(lambda : print("clip update"))
    """
    @staticmethod
    def listen(callback, interval=0.1):
        """Watch Clipboard Update, if updated, run callback without arguments.

        :param callback: a function without parameters.
        :param float interval: interval to check update.
        """
        clip_seq = wc.GetClipboardSequenceNumber()
        while True:
            clip_seq_new = wc.GetClipboardSequenceNumber()
            if clip_seq != clip_seq_new:
                clip_seq = clip_seq_new
                callback()
            else:
                sleep(interval)

    @staticmethod
    def read(format=None) -> bytes:
        """read data from clipboard

        :param int format: the clipboard format from winuser.h, ``CF_*`` constants.
                           if ``None``, will use first format which ``EnumClipboardFormats`` return.
        """
        if format is None:
            format = ClipBoard.enum_clipformats()[0]
        try:
            wc.OpenClipboard()
            data = wc.GetClipboardData(format)
        finally:
            wc.CloseClipboard()
        return data

    @staticmethod
    def write(data, format=wc.CF_UNICODETEXT):
        """write contents to clipboard.

        :param data: str or bytes
        :param int format: constants defined in winuser.h, the clipboard format.
        """
        try:
            wc.OpenClipboard()
            wc.EmptyClipboard()
            wc.SetClipboardData(format, data)
        finally:
            wc.CloseClipboard()

    @staticmethod
    def enum_clipformats() -> list:
        """枚举当前剪贴板中的数据格式"""
        formats = []
        fm = 0
        try:
            wc.OpenClipboard()
            while True:
                fm = wc.EnumClipboardFormats(fm)
                if fm != 0:
                    formats.append(fm)
                else:
                    break
        finally:
            wc.CloseClipboard()
        return formats
