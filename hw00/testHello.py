"""
@author: Carson Lee
"""
import unittest

class TestHello(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testHello(self): 
        self.assertEqual(1,1,'one equals one')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()