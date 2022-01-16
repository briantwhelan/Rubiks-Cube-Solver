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
       
    def tearDown(self):
        print("Tearing down test environment...")
        
    def testSolveRubiksCube(self):
        self.assertEqual(rubiksCubeSolver.solveRubiksCube(), False)
   
if __name__=='__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTests([TestRubiksCubeSolver("testSolveRubiksCube")])
    fileHandle = open("testReport.txt", "w")
    runner = unittest.TextTestRunner(fileHandle)
    runner.run(testSuite)
