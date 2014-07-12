# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power, enable_cache_for
from config import args, DEBUG
from copy import copy
import itertools

def charger_h(c, sensors, p_list):
    """calculate h for charger c(x, y) independently"""
    (ratio, h) = max([(total_power(sensors, p_list, [c], [h])/power(h), h) for h in xrange(args['h_max'] + 1)])
    return h

def power_levels(chargers, sensors, p_list):
    """return a list of h"""
    return [charger_h(c, sensors, p_list) for c in chargers];

def greedy(chargers, h_list, sensors, p_list):
    """greedy part"""
    # initialize
    Budget = args['B']
    b = 0
    Q = 0
    result_c = [];
    result_h = [];

    while b < Budget:
        max_power = 0
        max_delta = 0
        max_cost = 0
        max_index = None
        b_left = Budget - b

        # find the charger which can increase the total power most
        for (index, (c, h)) in enumerate(zip(chargers, h_list)):
            cost = power(h)
            if cost < b_left:
                temp_Q = total_power(sensors, p_list, result_c + [c], result_h + [h])
                if temp_Q - Q > max_delta:
                    max_power = temp_Q
                    max_delta = temp_Q - Q
                    max_cost = cost
                    max_index = index

        # greedy the charger we found
        if max_index:
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

def greedy_with_base(chargers, h_list, sensors, p_list, base):
    """return solution based on an initial set"""
    Budget = args['B']
    b = 0
    Q = 0
    result_c = [];
    result_h = [];

    # initialize with base
    for index in base:
        result_c.append(chargers[index])
        result_h.append(h_list[index])
        b += power(h_list[index])

    for index in base[::-1]:
        del chargers[index]
        del h_list[index]

    if b > Budget:
        return (0, [], [])

    Q = total_power(sensors, p_list, result_c, result_h)

    while b < Budget:
        max_power = 0
        max_delta = 0
        max_cost = 0
        max_index = None
        b_left = Budget - b

        # find the charger which can increase the total power most
        for (index, (c, h)) in enumerate(zip(chargers, h_list)):
            cost = power(h)
            if cost < b_left:
                temp_Q = total_power(sensors, p_list, result_c + [c], result_h + [h])
                if (temp_Q - Q) / cost > max_delta:
                    max_power = temp_Q
                    max_delta = (temp_Q - Q) / cost
                    max_cost = cost
                    max_index = index

        # greedy the charger we found
        if max_index:
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
        print "#        sub-result of k-choice part        #"
        print "============================================="
        pprint(result)

    return result

def k_choice(chargers, h_list, sensors, p_list, k):
    """k-choices-based algorithm part"""
    Q = 0
    result_c = [];
    result_h = [];

    for base in itertools.combinations(xrange(len(chargers)), k):
        (sub_Q, sub_c, sub_h) = greedy_with_base(copy(chargers), copy(h_list), sensors, p_list, base)
        if sub_Q > Q:
            (result_c, result_h) = (sub_c, sub_h)

    result = (Q, result_c, result_h)
    if DEBUG:
        print "============================================="
        print "#         result of k-choice part           #"
        print "============================================="
        pprint(result)

    return result


def ECalgorithm(chargers, h_list, sensors, p_list, k):
    """Enumeration-Complementary Algorithm, return (power, chargers, h_list)"""
    return max([greedy(copy(chargers), copy(h_list), sensors, p_list),
                k_choice(copy(chargers), copy(h_list), sensors, p_list, k),
            ])

def solution(chargers, sensors, p_list):
    """solution A body function"""
    # step 1: optimal power levels of all chargers
    h_list = power_levels(chargers, sensors, p_list)
    if (DEBUG):
        print "============================================="
        print "#           optimal power levels            #"
        print "============================================="
        pprint(h_list)

    # step 2: apply algorithm 3
    enable_cache_for(sensors, chargers, h_list)
    return ECalgorithm(chargers, h_list, sensors, p_list, args['k'])
