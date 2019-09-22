import unittest
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import PyCommons as pc


class TestIOModuleMethods(unittest.TestCase):

    def test_write_to_file(self):
        self.assertEqual(pc.write_to_file(output_file="test.txt", mode="w", text=""), True)
        self.assertEqual(pc.write_to_file(output_file="test.txt", mode="a", text="Hello"), True)



if __name__ == '__main__':
    unittest.main()