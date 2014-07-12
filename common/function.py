# -*- coding: utf-8 -*-

# make sure division can get float answer
from __future__ import division

from math import *
from config import args

def distance(c, s):
    """distance between point c(x, y) & s(x, y)."""
    (xc, yc) = c
    (xs, ys) = s

    return sqrt((xc-xs)**2 + (yc-ys)**2)

def power(h):
    """power of c(x, y)"""
    p_min = args['p_min']
    p_max = args['p_max']
    h_max = args['h_max']

    return p_min + float(h)/h_max * (p_max-p_min)

def func_D(h):
    """max charging distance of c(x, y)"""
    alpha = args['alpha']
    beta = args['beta']
    p_th = args['p_th']

    return sqrt(alpha / p_th * power(h)) - beta

def power_charged(c, s, h):
    """power of c(x, y) to s(x, y)"""
    max_d = func_D(h)
    dis = distance(c, s)

    if dis <= max_d:
        alpha = args['alpha']
        beta = args['beta']

        return alpha/((distance(c, s)+beta)**2) * power(h)
    else:
        return 0

def power_received(s, p, chargers, h_list):
    """sensor s(x, y) with power consumption p received power from chargers[(x, y), (x, y), ...]"""
    return sum([min(power_charged(c, s, h), p) for (c, h) in zip(chargers, h_list)])

def total_power(sensors, p_list, chargers, h_list):
    """total power"""
    return sum([power_received(s, p, chargers, h_list) for (s, p) in zip(sensors, p_list)])
