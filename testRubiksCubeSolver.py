import unittest

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
        self.assertEqual(True, False)
   
if __name__=='__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTests([TestRubiksCubeSolver("testSolveRubiksCube")])
    runner = unittest.TextTestRunner()
    runner.run(testSuite)