'''
Created on 30.10.2017

@author: pho
'''
import unittest
from root.raspradio.fade_in import start_fade_in


class FadeInTest(unittest.TestCase):


    def testName(self):
        start_fade_in()
        pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FadeInTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 