# -*- coding: utf-8 -*-

from config import args
from point import add_point_to
from point import random_point

import random

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

def rand_path():
    """
    random path
    """
    m = args['M']
    size = args['size']
    t_min = args['t_min']
    t_max = args['t_max']
    result = []

    for i in xrange(m):
        time_slice = []
        n = random.randint(t_min, t_max)

        temp = [random.random() for j in xrange(n)]
        total = sum(temp)
        weights = [t / total for t in temp]

        for j in xrange(n):
            x, y = random_point(*size)
            time_slice.append(((i, x, y), weights[j]))

        result.append(time_slice)

    return result
