
class Cell():
    """This class represents one cell of the rubics cube"""

    def __init__(self, loc: tuple, norm: tuple, color: int):
        self.location = loc
        self.normal = norm
        self.color = color

    def getLocation(self) -> tuple:
        return self.location

    def setLocation(self, loc: tuple):
        self.location = loc

    def getNormal(self) -> tuple:
        return self.normal

    def setNormal(self, norm: tuple):
        self.normal = norm

    def getColorNum(self):
        return self.color

    def getColor(self):
        return ['R', 'W', 'O', 'Y', 'B', 'G'][self.color]

    def getXTermColor(self):
        _ = {"R": "\x1b[48;5;160m",
           "Y": "\x1b[48;5;226m",
           "G": "\x1b[48;5;76m",
           "W": "\x1b[48;5;15m",
           "O": "\x1b[48;5;214m",
           "B": "\x1b[48;5;27m",
           "?": "\x1b[40m"}

        return _[self.getColor()] + "  \x1b[49m"
