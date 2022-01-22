class Face():
    def __init__(self):
        self.name = "face"

class RubiksCube():
    def __init__(self):
        self.faces = [Face(), Face(), Face(), Face(), Face(), Face()]
        self.solved = True

    def solve(self):
        return self.solved
