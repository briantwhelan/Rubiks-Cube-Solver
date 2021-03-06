import unittest
import rubiksCubeSolver

class TestRubiksCubeSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up test class...")
            
    @classmethod
    def tearDownClass(cls):
        print("Tearing down test class...")

    def setUp(self):
        print("Setting up test environment...")
        self.rubiksCube = rubiksCubeSolver.RubiksCube("WWWYYYWWW YYYWWWYYY RRROOORRR OOORRROOO BBBGGGBBB GGGBBBGGG")
        self.solvedRubiksCube = rubiksCubeSolver.RubiksCube("SOLVED")
       
    def tearDown(self):
        print("Tearing down test environment...")

    def testValidatingUserInput(self):
        self.assertTrue(rubiksCubeSolver.isValidInput(["RANDOM"]))
        self.assertTrue(rubiksCubeSolver.isValidInput(["rAnDoM"]))
        self.assertTrue(rubiksCubeSolver.isValidInput(["SOLVED"]))
        self.assertTrue(rubiksCubeSolver.isValidInput(["sOlVeD"]))
        self.assertTrue(rubiksCubeSolver.isValidInput(["WWWYYYWWW YYYWWWYYY RRROOORRR OOORRROOO BBBGGGBBB GGGBBBGGG"]))
        self.assertTrue(rubiksCubeSolver.isValidInput(["WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO BBBBBBBBB GGGGGGGGG"]))
        self.assertFalse(rubiksCubeSolver.isValidInput(["test"]))
        self.assertFalse(rubiksCubeSolver.isValidInput(["test", "test"]))

    def testReadingUserInput(self):
        self.assertEqual(rubiksCubeSolver.splitFaceIntoPieces("RRRRRRRRR"), ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'])
        self.assertEqual(rubiksCubeSolver.splitFaceIntoPieces("WYROBGWYR"), ['W', 'Y', 'R', 'O', 'B', 'G', 'W', 'Y', 'R'])
        self.assertEqual(rubiksCubeSolver.splitRubiksCubeIntoFaces("WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO BBBBBBBBB GGGGGGGGG"), ["WWWWWWWWW", "YYYYYYYYY", "RRRRRRRRR", "OOOOOOOOO", "BBBBBBBBB", "GGGGGGGGG"])
        self.assertEqual(rubiksCubeSolver.splitRubiksCubeIntoFaces("WWWYYYWWW YYYWWWYYY RRROOORRR OOORRROOO BBBGGGBBB GGGBBBGGG"), ["WWWYYYWWW", "YYYWWWYYY", "RRROOORRR", "OOORRROOO", "BBBGGGBBB", "GGGBBBGGG"])

    def testIsOneColourOnFace(self):
        face1 = rubiksCubeSolver.Face('F', "WWWWWWWWW")
        self.assertTrue(face1.isOneColour())
        face2 = rubiksCubeSolver.Face('F', "WWWYYYWWW")
        self.assertFalse(face2.isOneColour())

    def testNumberOfRubiksCubeFaces(self):
        numberOfRubiksCubeFaces = len(self.rubiksCube.faces)
        self.assertEqual(numberOfRubiksCubeFaces, 6)
        
    def testNumberOfPiecesOnEachFace(self):
        for face in self.rubiksCube.faces:    
            self.assertEqual(len(face.pieces), 9) 
        
    def testFaceEquality(self):
        face1 = rubiksCubeSolver.Face('F', "WWWWWWWWW")
        face2 = rubiksCubeSolver.Face('F', "WWWWWWWWW")
        self.assertEqual(face1, face2)
        face3 = rubiksCubeSolver.Face('F', "YYYYYYYYY")
        self.assertNotEqual(face1, face3)

    def testRubiksCubeEquality(self):
        self.assertEqual(self.rubiksCube, rubiksCubeSolver.RubiksCube("WWWYYYWWW YYYWWWYYY RRROOORRR OOORRROOO BBBGGGBBB GGGBBBGGG"))
    
    def testIsRubiksCubeSolved(self):
        self.assertFalse(self.rubiksCube.isSolved())
        self.assertTrue(self.solvedRubiksCube.isSolved())

    def testSolveRubiksCube(self):
        self.assertEqual(self.rubiksCube.solve(), self.solvedRubiksCube.solve())
    
if __name__=='__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTests([TestRubiksCubeSolver("testValidatingUserInput"), TestRubiksCubeSolver("testReadingUserInput"),
                        TestRubiksCubeSolver("testNumberOfRubiksCubeFaces"), TestRubiksCubeSolver("testNumberOfPiecesOnEachFace"), 
                        TestRubiksCubeSolver("testIsOneColourOnFace"), TestRubiksCubeSolver("testFaceEquality"), TestRubiksCubeSolver("testRubiksCubeEquality")])
    testSuite.addTests([TestRubiksCubeSolver("testSolveRubiksCube")])
    fileHandle = open("testReport.txt", "w")
    runner = unittest.TextTestRunner(fileHandle)
    runner.run(testSuite)
