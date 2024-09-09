import unittest
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from main import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(1,2), 3)

if __name__ == '__main__':
    unittest.main()