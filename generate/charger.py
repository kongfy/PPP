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
    d = args['D']
    result = []

    length = min(n/d, m/d)
    n /= length
    m /= length
    cid = 0

    for x in xrange(n):
        for y in xrange(m):
            result.append((cid, (x+0.5) * length, (y+0.5) * length))
            cid += 1

    return result
