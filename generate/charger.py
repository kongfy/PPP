# -*- coding: utf-8 -*-

from config import args
from point import add_point_to

def rand():
    """randomly distributed"""
    n = args['N']
    size = args['size']
    result = []
    for i in xrange(n):
        add_point_to(result, *size)
    return result

def regular():
    """regularly distributed"""
    pass
