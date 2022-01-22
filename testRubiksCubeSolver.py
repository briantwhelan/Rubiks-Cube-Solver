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
        
    def testStateOfRubiksCube(self):
        self.assertEqual(len(self.rubiksCube.faces), 6)
        for face in self.rubiksCube.faces:    
            self.assertEqual(len(face.pieces), 9)

    def testSolveRubiksCube(self):
        self.assertEqual(self.rubiksCube.solve(), self.solvedRubiksCube.solved)
    
if __name__=='__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTests([TestRubiksCubeSolver("testStateOfRubiksCube"), TestRubiksCubeSolver("testSolveRubiksCube")])
    fileHandle = open("testReport.txt", "w")
    runner = unittest.TextTestRunner(fileHandle)
    runner.run(testSuite)
