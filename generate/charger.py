# -*- coding: utf-8 -*-

from config import args
from point import random_point

"""
randomly distributed
"""
def random():
    n = args['N']
    size = args['size']
    # WARNING: may have some conflict points
    return [(random_point(*size), random_point(*size)) for i in xrange(n)]

"""
regularly distributed
"""
def regular():
    pass
