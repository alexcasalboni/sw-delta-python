#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" sw_delta main logic (files wrapping) """
from os.path import exists
from mimetypes import guess_type

from sw_delta.calculator import calculate_delta
from sw_delta.exceptions import InvalidAskedFile, InvalidCachedFile

def get_delta(asked_file_path, cached_file_path):
    """ Return a tuple of (body, mime_type), given two file paths """

    if not exists(asked_file_path):
        raise InvalidAskedFile("%s not found." % asked_file_path)

    if not exists(cached_file_path):
        raise InvalidCachedFile("%s not found." % asked_file_path)

    with open(asked_file_path, 'r') as filep:
        asked_file_string = filep.read()

    with open(cached_file_path, 'r') as filep:
        cached_file_string = filep.read()

    body = calculate_delta(asked_file_string, cached_file_string)
    mime_type = "text/sw-delta"

    if len(body) > len(asked_file_string):
        body = asked_file_string
        mime_type, _ = guess_type(asked_file_path)

    return body, mime_type
