"""调用外部功能

latex
imagemagick
"""


class XeLaTeX:
    def __init__(self, **options):
        pass

    @property
    def command(self) -> list:
        return ["xelatex", ]

    def do(self, obj):
        pass


class ImageMagick:
    def __init__(self, **options):
        pass

    @property
    def command(self):
        return ["imagemagick"]

    def do(self, obj):
        pass
