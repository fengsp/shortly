# -*- coding: utf-8 -*-
"""
    shortly.utils
    ~~~~~~~~~~~~~

    Shortly utils.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""

from urlparse import urlparse


def is_valid_url(url):
    parts = urlparse(url)
    return parts.scheme in ('http', 'https')


def base52_encode(number):
    assert isinstance(number, int), 'integer required'
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base52 = []
    while number != 0:
        number, i = divmod(number, 52)
        base52.append('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[i])
    return ''.join(reversed(base52))
