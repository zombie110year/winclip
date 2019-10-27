"""剪贴板

监听剪贴板变动
读写剪贴板
"""
import win32.win32clipboard as wc
from time import sleep


class ClipBoard:
    @staticmethod
    def listen(callback, interval=0.1):
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
        if format is None:
            format = enum_clipformats()[0]
        try:
            wc.OpenClipboard()
            data = wc.GetClipboardData(format)
        finally:
            wc.CloseClipboard()
        return data

    @staticmethod
    def write(data: bytes, format=wc.CF_UNICODETEXT):
        try:
            wc.OpenClipboard()
            wc.EmptyClipboard()
            wc.SetClipboardData(format, data)
        finally:
            wc.CloseClipboard()


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
