import unittest
import os, sys, inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import PyCommons as pc


class TestGenricModuleMethods(unittest.TestCase):
    
    def test_(self):
        self.assertEqual(int(pc.get_unix_timestamp()), int(time.time()))



if __name__ == '__main__':
    unittest.main()