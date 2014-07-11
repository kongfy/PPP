# -*- coding: utf-8 -*-

from math import *
from config import args

# make sure division can get float answer
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
    p_min = args['p_min']
    p_max = args['p_max']
    h_max = args['h_max']

    return p_min + float(h)/h_max * (p_max-p_min)


"""
max charging distance of c(x, y)
"""
def func_D(h):
    alpha = args['alpha']
    beta = args['beta']
    p_th = args['p_th']

    return sqrt(alpha / p_th * power(h)) - beta

"""
power of c(x, y) to s(x, y)
"""
def power_charged(c, s, h):
    max_d = func_D()
    dis = distance(c, s)

    if dis <= max_d:
        alpha = args['alpha']
        beta = args['beta']

        return alpha/((distance(c, s)+beta)**2) * power(h)
    else:
        return 0


"""
sensor s(x, y) with power consumption p received power from chargers[(x, y), (x, y), ...]
"""
def power_received(s, p, chargers, h_list):
    return sum([min(power_charged(c, s, h), p) for (c, h) in zip(chargers, h_list)])

"""
total power
"""
def total_power(sensors, p_list, chargers, h_list):
    return sum([power_received(s, p, chargers, h_list) for (s, p) in zip(sensor, p_list)])
