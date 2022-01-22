import enum

class Colour(enum.Enum):
    white = 0
    yellow = 1
    red = 2
    orange = 3
    blue = 4
    green = 5

class Face():
    def __init__(self):
        self.name = "face"
        self.pieces = [Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white]

class RubiksCube():
    def __init__(self):
        self.faces = [Face(), Face(), Face(), Face(), Face(), Face()]
        self.solved = True

    def solve(self):
        return self.solved
