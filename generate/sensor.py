# -*- coding: utf-8 -*-

from config import args
from point import add_point_to

def rand():
    """randomly distributed"""
    m = args['M']
    size = args['size']
    result = []
    for i in xrange(m):
        add_point_to(result, *size)
    return result
