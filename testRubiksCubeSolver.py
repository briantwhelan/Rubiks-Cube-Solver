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
        self.rubiksCube = rubiksCubeSolver.RubiksCube()
        self.solvedRubiksCube = rubiksCubeSolver.RubiksCube()
       
    def tearDown(self):
        print("Tearing down test environment...")

    def testIsOneColourOnFace(self):
        face1 = rubiksCubeSolver.Face(rubiksCubeSolver.TempFace.front)
        self.assertTrue(face1.isOneColour())
        face2 = rubiksCubeSolver.Face(rubiksCubeSolver.TempFace.up)
        self.assertFalse(face2.isOneColour())

    def testNumberOfRubiksCubeFaces(self):
        numberOfRubiksCubeFaces = len(self.rubiksCube.faces)
        self.assertEqual(numberOfRubiksCubeFaces, 6)
        
    def testNumberOfPiecesOnEachFace(self):
        for face in self.rubiksCube.faces:    
            self.assertEqual(len(face.pieces), 9)
        
    def testColoursOnFaces(self):
        self.assertEqual(self.rubiksCube.isValid(), True) 
        
    def testFaceEquality(self):
        face1 = rubiksCubeSolver.Face(rubiksCubeSolver.TempFace.front)
        face2 = rubiksCubeSolver.Face(rubiksCubeSolver.TempFace.front)
        self.assertEqual(face1, face2)
        face3 = rubiksCubeSolver.Face(rubiksCubeSolver.TempFace.back)
        self.assertNotEqual(face1, face3)

    def testRubiksCubeEquality(self):
        self.assertEqual(self.rubiksCube, rubiksCubeSolver.RubiksCube())

    def testSolveRubiksCube(self):
        self.assertEqual(self.rubiksCube.solve(), self.solvedRubiksCube.solved)
    
if __name__=='__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTests([TestRubiksCubeSolver("testNumberOfRubiksCubeFaces"), TestRubiksCubeSolver("testNumberOfPiecesOnEachFace"), 
                        TestRubiksCubeSolver("testColoursOnFaces"), TestRubiksCubeSolver("testFaceEquality"), 
                        TestRubiksCubeSolver("testRubiksCubeEquality")])
    testSuite.addTests([TestRubiksCubeSolver("testSolveRubiksCube")])
    fileHandle = open("testReport.txt", "w")
    runner = unittest.TextTestRunner(fileHandle)
    runner.run(testSuite)
