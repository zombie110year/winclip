import win32.win32clipboard as wc

from clip2tex.clipboard import ClipBoard


def test_rw_text():
    text = "Hello World"
    ClipBoard.write(text)
    text_r = ClipBoard.read(wc.CF_UNICODETEXT)
    assert text == text_r
    text_rb = ClipBoard.read(wc.CF_OEMTEXT)
    assert text_rb == text.encode("ascii")


def test_rw_bitmap():
    with open("tests/msdn-logo.bmp", "rb") as bmp:
        data = bmp.read()
    ClipBoard.write(data, wc.CF_DIB)

    data1 = ClipBoard.read(wc.CF_DIB)

    # data1 尾部会多一个 0x00
    assert data1.startswith(data)
