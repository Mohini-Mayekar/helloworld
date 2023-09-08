import unittest

class TestScript(unittest.TestCase):

    def testHello(self): 
        self.assertEqual(1,1,'one equals one')

if __name__ == '__main__':
    print("Executing unit test cases")
    unittest.main()