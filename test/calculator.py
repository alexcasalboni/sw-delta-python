#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from sw_delta.calculator import calculate_delta, SEPARATORS
from sw_delta.exceptions import SeparatorException

class TestDeltaCalculator(unittest.TestCase):
    
    def setUp(self):
        """ TestCase setup """
    
    def test_strings(self):
        """ DeltaCalculator - string """
        s1 = "this is some test. blah blah blah"
        s2 = "this is other text. blah blah blah"
        delta = calculate_delta(s1, s2)

        self.assertTrue(delta)
        self.assertTrue(len(delta) < len(s2))

    def test_unicode(self):
        """ DeltaCalculator - unicode """
        s1 = u"this is some test. blah blah blah"
        s2 = u"this is other text. blah blah blah"
        delta = calculate_delta(s1, s2)

        self.assertTrue(delta)
        self.assertTrue(len(delta) < len(s2))

    def test_separator_equals(self):
        """ DeltaCalculator - separator (in both strings -> no separator in delta) """
        for sep in SEPARATORS:
            s1 = "%sthis is some test. blah blah blah" % sep
            s2 = "%sthis is other text. blah blah blah" % sep
            delta = calculate_delta(s1, s2)

            self.assertTrue(delta)
            self.assertEqual(0, delta.count(sep))

    def test_separator_new(self):
        """ DeltaCalculator - separator (only new string -> delta will contain it too!) """
        for sep in SEPARATORS:
            s1 = "this is some text. blah blah blah"
            s2 = "%sthis is some text. blah blah blah" % sep
            delta = calculate_delta(s1, s2)

            self.assertTrue(delta)
            self.assertEqual(1, delta.count(sep))

    def test_separator_new(self):
        """ DeltaCalculator - separator (only new string -> delta will contain it too!) """
        all_separators = "".join(SEPARATORS)
        s1 = "%sthis is some text. blah blah blah" % all_separators
        s2 = "%sthis is some text. blah blah blah" % all_separators

        # all separators are used -> exception
        with self.assertRaises(SeparatorException):
            delta = calculate_delta(s1, s2)
