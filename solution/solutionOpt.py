# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power
from config import args, DEBUG
from copy import copy


# global variables
g_Q = 0
g_result = None
g_C = []
g_H = []
g_B = args['B']

def update(sensors, p_list):
    """update anser"""
    global g_Q
    global g_result
    global g_C
    global g_H

    temp_Q = total_power(sensors, p_list, g_C, g_H)
    if temp_Q > g_Q:
        g_Q = temp_Q
        g_result = (copy(g_C), copy(g_H))
        """
        if DEBUG:
            print g_result, g_Q
        """


def solve(chargers, n, cost, sensors, p_list):
    """
    n is the number of chargers have already been considered,
    enumerate every possible choise using dfs
    """
    global g_C
    global g_H

    if n == len(chargers):
        update(sensors, p_list)
        return

    # don't chose this charger
    solve(chargers, n + 1, cost, sensors, p_list)

    # chose it by every possible h
    c = chargers[n]
    for h in xrange(1, args['h_max'] + 1):
        if power(h) + cost > g_B:
            break
        g_C.append(c)
        g_H.append(h)
        solve(chargers, n + 1, cost + power(h), sensors, p_list)
        del g_C[len(g_C) - 1]
        del g_H[len(g_H) - 1]

def solution(chargers, sensors, p_list):
    """
    solution Opt body function.
    so agly...so sad...dfs
    """
    if DEBUG:
        print "============================================="
        print "#                update trace               #"
        print "============================================="

    solve(chargers, 0, 0, sensors, p_list)

    global g_Q
    global g_result

    (C, H) = g_result
    return (g_Q, C, H)
