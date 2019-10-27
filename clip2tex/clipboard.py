"""剪贴板

监听剪贴板变动
读写剪贴板
"""
import win32.win32clipboard as wc


class ClipBoard:
    @staticmethod
    def listen():
        pass

    @staticmethod
    def read(format=wc.CF_UNICODETEXT) -> bytes:
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
