import win32.win32clipboard as wc

from clip2tex.clipboard import ClipBoard


def test_rw_text():
    text = "Hello World"
    ClipBoard.write(text)
    text_r = ClipBoard.read()
    assert text == text_r
