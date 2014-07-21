# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power
from config import args, DEBUG
from copy import copy

def charger_h(c, sensors, p_list):
    """calculate h for charger c(x, y) independently"""
    (ratio, h) = max([(total_power(sensors, p_list, [c], [h])/power(h), h) for h in xrange(1, args['h_max'] + 1)])
    return h

def power_levels(chargers, sensors, p_list):
    """return a list of h"""
    return [charger_h(c, sensors, p_list) for c in chargers];

def delta_one(delta, cost):
    return delta

def delta_two(delta, cost):
    return delta / cost

def greedy(chargers, h_list, sensors, p_list, func):
    """greedy part"""
    # initialize
    Budget = args['B']
    b = 0
    Q = 0
    result_c = []
    result_h = []

    while b < Budget:
        max_power = 0
        max_delta = 0
        max_cost = 0
        max_index = None
        b_left = Budget - b

        # find the charger which can increase the total power most
        for (index, (c, h)) in enumerate(zip(chargers, h_list)):
            cost = power(h)
            if cost <= b_left:
                temp_Q = total_power(sensors, p_list, result_c + [c], result_h + [h])
                delta = func(temp_Q - Q, cost)
                if delta > max_delta:
                    max_power = temp_Q
                    max_delta = delta
                    max_cost = cost
                    max_index = index

        # greedy the charger we found
        if max_index != None:
            Q = max_power
            b += max_cost
            result_c.append(chargers[max_index])
            result_h.append(h_list[max_index])
            del chargers[max_index]
            del h_list[max_index]
        else:
            break

    result = (Q, result_c, result_h)
    if DEBUG:
        print "============================================="
        print "#           result of greedy part           #"
        print "============================================="
        pprint(result)

    return result

def TCBalgorithm(chargers, h_list, sensors, p_list):
    """Two Choices-based Algorithm, return (power, chargers, h_list)"""
    return max(greedy(copy(chargers), copy(h_list), sensors, p_list, delta_one),
               greedy(copy(chargers), copy(h_list), sensors, p_list, delta_two),
               )

def solution(chargers, sensors, p_list):
    """solution A body function"""
    # step 1: optimal power levels of all chargers
    h_list = power_levels(chargers, sensors, p_list)
    if (DEBUG):
        print "============================================="
        print "#           optimal power levels            #"
        print "============================================="
        pprint(h_list)

    # step 2: apply algorithm 2
    return TCBalgorithm(chargers, h_list, sensors, p_list)
