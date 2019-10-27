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
        pass

    @staticmethod
    def write(data: bytes, format=wc.CF_UNICODETEXT):
        pass
