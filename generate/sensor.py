# -*- coding: utf-8 -*-

from config import args
from point import add_point_to
from point import random_point

def rand():
    """randomly distributed"""
    m = args['M']
    size = args['size']
    result = []
    for i in xrange(m):
        time_slice = []
        x, y = random_point(*size)
        time_slice.append(((i, x, y), 1))
        result.append(time_slice)

    return result
