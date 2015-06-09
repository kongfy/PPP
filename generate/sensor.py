# -*- coding: utf-8 -*-

from config import args
from point import add_point_to
from point import random_point

import random
import math

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

def next_location(x, y):
    n, m = args['size']
    edge = (n + m) / 2.0
    r = random.uniform(0, 2) * math.pi
    d = random.uniform(0, edge * args['hop'])

    x += math.cos(r) * d
    y += math.sin(r) * d

    while x < 0 or x > n or y < 0 or y > m:
        if x < 0:
            x = -x
        elif x > n:
            x = n - (x - n)
        elif y < 0:
            y = -y
        elif y > m:
            y = m - (y - m)

    return (x, y)

def rand_trace():
    """
    random trace
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

        x, y = random_point(*size)
        for j in xrange(n):
            time_slice.append(((i, x, y), weights[j]))
            x, y = next_location(x, y)

        result.append(time_slice)

    return result
