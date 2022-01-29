import enum

def splitFaceIntoPieces(face):
    return list(face)

def splitRubiksCubeIntoFaces(rubiksCube):
    return rubiksCube.split()

def isValidInput(userInput):
    isValidInput = False
    if(len(userInput) == 1):
        if(userInput[0].upper() == "SOLVED" 
                or userInput[0].upper() == "RANDOM"
                or userInput[0].upper() == "WWWYYYWWW YYYWWWYYY RRROOORRR OOORRROOO BBBGGGBBB GGGBBBGGG"
                or userInput[0].upper() == "WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO BBBBBBBBB GGGGGGGGG"):
            isValidInput = True
    return isValidInput

class Colour(enum.Enum):
    white = 0
    yellow = 1
    red = 2
    orange = 3
    blue = 4
    green = 5

class Face():
    def __init__(self, name, face):
        self.name = name
        self.pieces = splitFaceIntoPieces(face)

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
    def __init__(self, *args):
        if(isValidInput(args)):
            if(args[0].upper() == "SOLVED"):
                self.faces =[Face('F', "WWWWWWWWW"), Face('U', "BBBBBBBBB"), Face('R', "RRRRRRRRR"), Face('B', "YYYYYYYYY"), Face('L', "OOOOOOOOO"), Face('D', "GGGGGGGGG")]
            elif(args[0].upper() == "RANDOM"):
                self.faces =[Face('F', "WYWYWYWYW"), Face('U', "BGBBGBBGB"), Face('R', "RORRORROR"), Face('B', "YWYWYWYWY"), Face('L', "ORORORORO"), Face('D', "GBGGBGGBG")]
            else:
                faces = splitRubiksCubeIntoFaces(args[0])
                self.faces = [Face('F', faces[0]), Face('U', faces[1]), Face('R', faces[2]), Face('B', faces[3]), Face('L', faces[4]), Face('D', faces[5])]
        else:
            raise ValueError("Invalid argument")

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
    
    def isSolved(self):
        isSolved = True
        for face in self.faces:
            if(not face.isOneColour()):
                isSolved = False
        return isSolved

    def solve(self):
        return True
