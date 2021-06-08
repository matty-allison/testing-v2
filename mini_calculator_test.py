import unittest
from python_testing import MyMiniCalculator

class TestMiniCalculator(unittest.TestCase):
    def test_add(self):
        add_object = MyMiniCalculator()
        self.assertEqual(add_object.add(1, 1), 2), "Incorrect Addition. Answer should be two"
