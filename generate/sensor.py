# -*- coding: utf-8 -*-

from config import args
from point import random_point

def random():
    """randomly distributed"""

    m = args['M']
    size = args['size']
    # WARNING: may have some conflict points
    return [(random_point(*size), random_point(*size)) for i in xrange(m)]
