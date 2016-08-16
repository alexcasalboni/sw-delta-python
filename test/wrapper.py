import unittest
import os
from sw_delta import get_delta


class TestDelta(unittest.TestCase):

    def _build_path(self, filepath):
        """ Build absolute reference to fixture file """
        return os.path.join(
            os.path.dirname(__file__),
            'fixtures',
            filepath,
        )
    
    def setUp(self):
        """ TestCase setup """
        self.path1 = self._build_path("f1.txt")
        self.path2 = self._build_path("f2.txt")
    
    def test_simple(self):
        """ DeltaCalculator - simple """

        body, mimetype = get_delta(self.path1, self.path2)

        self.assertTrue(body)
        self.assertTrue(mimetype)
        self.assertEqual(mimetype, "text/sw-delta")
       