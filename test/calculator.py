import unittest
from sw_delta.calculator import calculate_delta

class TestDeltaCalculator(unittest.TestCase):
    
    def setUp(self):
        """ TestCase setup """
        self.s1 = "this is some test. blah blah blah"
        self.s2 = "this is other text. blah blah blah"
    
    def test_simple(self):
        """ DeltaCalculator - simple """

        delta = calculate_delta(self.s1, self.s2)

        self.assertTrue(delta)
        self.assertTrue(len(delta) < len(self.s2))
       