#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists
from mimetypes import guess_type

from sw_delta.calculator import calculate_delta
from sw_delta.exceptions import InvalidAskedFile, InvalidCachedFile

def get_delta(asked_file_path, cached_file_path):

    if not exists(asked_file_path):
        raise InvalidAskedFile("%s not found." % asked_file_path)

    if not exists(cached_file_path):
        raise InvalidCachedFile("%s not found." % asked_file_path)


    with open(asked_file_path, 'r') as f:
        asked_file_string = f.read()

    with open(cached_file_path, 'r') as f:
        cached_file_string = f.read()

    body = calculate_delta(asked_file_string, cached_file_string)
    mime_type = "text/sw-delta"

    if len(body) > len(asked_file_string):
        body = asked_file_string
        mime_type, _encoding = guess_type(asked_file_path)

    return body, mime_type
