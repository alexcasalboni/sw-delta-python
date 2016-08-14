#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InvalidFile(IOError):
    """ Raised when a file is missing """

class InvalidAskedFile(InvalidFile):
    """ Raised when the asked file is missing """

class InvalidCachedFile(InvalidFile):
    """ Raised when the cached file is missing """