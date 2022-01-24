import enum

class Colour(enum.Enum):
    white = 0
    yellow = 1
    red = 2
    orange = 3
    blue = 4
    green = 5

class TempFace(enum.Enum):
    front = 0
    up = 1
    right = 2
    back = 3
    left = 4
    down = 5

class Face():
    def __init__(self, face):
        self.name = face.name
        if(face == TempFace.front):
            self.pieces = [Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white, Colour.white]
        elif(face == TempFace.up):
            self.pieces = [Colour.green, Colour.blue, Colour.blue, Colour.blue, Colour.blue, Colour.blue, Colour.blue, Colour.blue, Colour.blue]
        elif(face == TempFace.right):
            self.pieces = [Colour.red, Colour.red, Colour.red, Colour.red, Colour.red, Colour.red, Colour.red, Colour.red, Colour.red]
        elif(face == TempFace.back):
            self.pieces = [Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow, Colour.yellow]
        elif(face == TempFace.left):
            self.pieces = [Colour.orange, Colour.orange, Colour.orange, Colour.orange, Colour.orange, Colour.orange, Colour.orange, Colour.orange, Colour.orange]
        elif(face == TempFace.down):
            self.pieces = [Colour.blue, Colour.green, Colour.green, Colour.green, Colour.green, Colour.green, Colour.green, Colour.green, Colour.green]
    
    def __eq__(self, other):
        if(isinstance(other, Face)):
            return self.name == other.name and self.pieces == other.pieces
        else:
            return False

    def isOneColour(self):
        isOneColour = True
        for piece1 in self.pieces:
            for piece2 in self.pieces:
                if(piece1 != piece2):
                    isOneColour = False
        return isOneColour

class RubiksCube():
    def __init__(self):
        self.faces = [Face(TempFace.front), Face(TempFace.up), Face(TempFace.right), Face(TempFace.back), Face(TempFace.left), Face(TempFace.down)]
        self.solved = True
    
    def __eq__(self, other):
        if(isinstance(other, RubiksCube)):
            return self.faces == other.faces
        else:
            return False

    def is6Faces(self):
        return (len(self.faces) == 6)

    def is9PiecesInEachFace(self):
        is9PiecesInEachFace = True
        for face in self.faces:
            if(len(face.pieces) != 9):
                is9PiecesInEachFace = False
        return is9PiecesInEachFace

    def is9PiecesOfEachColour(self):
        is9PiecesOfEachColour = True
        colourCount = {}
        for face in self.faces:
            for piece in face.pieces:
                if(piece in colourCount):
                    colourCount[piece] += 1
                else:
                    colourCount[piece] = 1
        
        for colour in colourCount: 
            if(colourCount[colour] != 9):
                is9PiecesOfEachColour = False
        return is9PiecesOfEachColour

    def isValid(self):
        return (self.is6Faces() and self.is9PiecesInEachFace() and self.is9PiecesOfEachColour())
    
    def solve(self):
        return self.solved
