# -*- coding: utf-8 -*-

from config import args
from point import add_point_to

def rand():
    """randomly distributed"""
    n = args['N']
    size = args['size']
    result = []
    for i in xrange(n):
        add_point_to(result, i, *size)
    return result

def fixed():
    """
    fixed ditributed
    """
    n, m = args['size']
    result = []

    cid = 0
    for x in xrange(n + 1):
        for y in xrange(m + 1):
            result.append((cid, x, y))
            cid += 1

    return result
