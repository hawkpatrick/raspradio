'''
Created on 15.10.2017

@author: pho
'''
import unittest

class RadioTest(unittest.TestCase):

    def testName(self):
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_upper']
    suite = unittest.TestLoader().loadTestsFromTestCase(RadioTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 
    
    
