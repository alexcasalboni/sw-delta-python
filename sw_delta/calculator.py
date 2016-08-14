#!/usr/bin/env python
# -*- coding: utf-8 -*-
from diff_match_patch import diff_unicode, diff_str


def calculate_delta(old_string, new_string):
    """ Return an optimized diff for sw-delta, given two strings """

    # find unused char as separator
    separator = '§'
    if separator in old_string or separator in new_string:
        separator = '␡'

    # Let's say we want to diff these two strings:
    # old_string = "this is some test. blah blah blah"
    # new_string = "this is other text. blah blah blah"

    # str Vs. unicode
    if isinstance(old_string, str) and isinstance(new_string, str):
        diff_f = diff_str
    else:
        diff_f = diff_unicode

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
    index = 0
    global_index = 0

    for diff in diffs:

        symbol = diff[0]
        n_chars = diff[1]

        if symbol in ('+', '-'):
            prefix = "%s%s%s" % (separator, index, symbol)
            new_chars = new_string[global_index:global_index+n_chars] if symbol == '+' else n_chars
            result += "%s%s" % (prefix, new_chars)
            index = 0

        if symbol in ('+', '='):
            global_index += n_chars

        if symbol == '=':
            index += n_chars

    # the output will be something like this:
    # §8-4§0+other§3-1§0+x

    return result
