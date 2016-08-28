#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Delta calculation logic (wrapping diff_match_path)  """
from diff_match_patch import diff_unicode, diff_str
from sw_delta.exceptions import SeparatorException

SEPARATORS = ('§', '␡')  # TODO add more alternatives!

def _choose_separator(old_string, new_string):
    """ Return a proper separator, based on the two input strings """
    separator = None

    for _sep in SEPARATORS:
        if not (_sep in str(old_string) or _sep in str(new_string)):
            separator = _sep
            break

    if not separator:
        raise SeparatorException("Couldn't find a proper separator")
    else:
        return separator

def calculate_delta(old_string, new_string):
    """ Return an optimized diff for sw-delta, given two strings """

    separator = _choose_separator(old_string, new_string)

    # Let's say we want to diff these two strings:
    # old_string = "this is some test. blah blah blah"
    # new_string = "this is other text. blah blah blah"

    # str Vs. unicode
    if isinstance(old_string, str) and isinstance(new_string, str):
        diff_f = diff_str
        print("using str diff")
    else:
        diff_f = diff_unicode
        print("using unicode diff")

    diffs = diff_f(old_string, new_string)

    # The output is a list of tuples, like these:
    # [
    #     ('=', 8),
    #     ('-', 4),
    #     ('+', 5),
    #     ('=', 3),
    #     ('-', 1),
    #     ('+', 1),
    #     ('=', 17)
    # ]

    result = ''
    offset = 0
    global_index = 0

    for diff in diffs:

        symbol = diff[0]
        n_chars = diff[1]

        if symbol in ('+', '-'):
            prefix = "%s%s%s" % (separator, offset, symbol)
            new_chars = new_string[global_index:global_index+n_chars] if symbol == '+' else n_chars
            result += "%s%s" % (prefix, str(new_chars))
            offset = 0

        if symbol in ('+', '='):
            global_index += n_chars

        if symbol == '=':
            offset += n_chars

    # the output will be something like this:
    # §8-4§0+other§3-1§0+x

    return result
