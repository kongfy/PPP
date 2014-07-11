# -*- coding: utf-8 -*-

from math import *
import config

# make sure division can get float anser
from __future__ import division

"""
distance between point c(x, y) & s(x, y)
"""
def distance(c, s):
    (xc, yc) = c
    (xs, ys) = s

    return sqrt((xc-xs)**2 + (yc-ys)**2)

"""
power of c(x, y)
"""
def power(h):
    p_min = config['p_min']
    p_max = config['p_max']
    h_max = config['h_max']

    return p_min + float(h)/h_max * (p_max-p_min)


"""
max charging distance of c(x, y)
"""
def func_D(h):
    alpha = config['alpha']
    beta = config['beta']
    p_th = config['p_th']

    return sqrt(alpha / p_th * power(h)) - beta

"""
power of c(x, y) to s(x, y)
"""
def power_charged(c, s, h):
    max_d = func_D()
    dis = distance(c, s)

    if dis <= max_d:
        alpha = config['alpha']
        beta = config['beta']

        return alpha/((distance(c, s)+beta)**2) * power(h)
    else:
        return 0


"""
sensor received power
"""
