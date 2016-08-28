#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" sw_delta custom exceptions """

class InvalidFile(IOError):
    """ Raised when a file is missing """

class InvalidAskedFile(InvalidFile):
    """ Raised when the asked file is missing """

class InvalidCachedFile(InvalidFile):
    """ Raised when the cached file is missing """

class SeparatorException(Exception):
    """ Raised when no separator could be chosen """
