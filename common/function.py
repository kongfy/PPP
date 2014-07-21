# -*- coding: utf-8 -*-

# make sure division can get float answer
from __future__ import division

from math import *
from config import args

def distance(c, s):
    """distance between point c(x, y) & s(x, y)."""
    (cid, xc, yc) = c
    (sid, xs, ys) = s

    return float(sqrt((xc-xs)**2 + (yc-ys)**2))

def power(h):
    """power of c(x, y)"""
    p_min = args['p_min']
    return h * p_min

def func_D(h):
    """max charging distance of c(x, y)"""
    alpha = args['alpha']
    beta = args['beta']
    p_th = args['p_th']

    return max(sqrt(alpha / p_th * power(h)) - beta, 0)

cache = {}
def power_charged(c, s, h):
    """power of c(x, y) to s(x, y)"""
    # use cache here
    global cache
    if cache.get((c, s, h), None) != None:
        return cache[(c, s, h)]

    max_d = func_D(h)
    dis = distance(c, s)

    if dis <= max_d:
        alpha = args['alpha']
        beta = args['beta']

        ans = alpha/((distance(c, s)+beta)**2) * power(h)
    else:
        ans = 0

    cache[(c, s, h)] = ans
    return ans

def power_received(s, p, chargers, h_list):
    """sensor s(x, y) with power consumption p received power from chargers[(x, y), (x, y), ...]"""
    return min(sum([power_charged(c, s, h) for (c, h) in zip(chargers, h_list)]), p)

def total_power(sensors, p_list, chargers, h_list):
    """total power"""
    return sum([power_received(s, p, chargers, h_list) for (s, p) in zip(sensors, p_list)])
