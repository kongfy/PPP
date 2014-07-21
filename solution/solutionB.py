# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power
from config import args, DEBUG
from copy import copy

def delta_one(delta, cost):
    return delta

def delta_two(delta, cost):
    return delta / cost

def greedy(chargers, sensors, p_list, func):
    """greedy algorithm, base on value function 'func'."""
    # initialize
    Budget = args['B']
    b = 0
    Q = 0
    H = {}

    # construct matrix Z
    Z = [[(c, h) for h in xrange(1, args['h_max'] + 1)] for c in chargers]
    # Z'
    temp_c = []
    temp_h = []

    while b < Budget:
        max_power = 0
        max_delta = 0
        max_cost = 0
        max_index = None
        b_left = Budget - b

        # find the best charger & h in matrix Z
        for (i, c_h_list) in enumerate(Z):
            for (j, (c, h)) in enumerate(c_h_list):
                cost = power(h)
                if cost <= b_left:
                    temp_Q = total_power(sensors, p_list, temp_c + [c], temp_h + [h])
                    delta = func(temp_Q - Q, cost)
                    if delta > max_delta:
                        max_power = temp_Q
                        max_delta = delta
                        max_cost = cost
                        max_index = (i, j)

        # greedy!!!
        if max_index != None:
            # add max charger in Z' & remove from Z
            Q = max_power
            b += max_cost
            (i, j) = max_index
            (c, h) = Z[i][j]
            temp_c.append(c)
            temp_h.append(h)
            del Z[i][j]

            # if H[c] < h then H[c] <== h
            H[c] = max(H.get(c, 0), h)
        else:
            break

    result = (Q, H, temp_c, temp_h)
    if DEBUG:
        print "============================================="
        print "#           result of greedy part           #"
        print "============================================="
        pprint(result)

    return H


def TCBalgorithm(chargers, sensors, p_list):
    """Two Choices-based Algorithm, return (Q, chargers, h_list)"""
    H1 = greedy(copy(chargers), sensors, p_list, delta_one)
    H2 = greedy(copy(chargers), sensors, p_list, delta_two)
    return max(budget_killer(H1, chargers, sensors, p_list),
               budget_killer(H2, chargers, sensors, p_list),
               )

def budget_killer(H, chargers, sensors, p_list):
    """utilize the remaining budget, return (Q, chargers, h_list)"""
    p_min = args['p_min']
    Budget = args['B']
    h_max = args['h_max']

    # current cost
    cost = 0
    for (c, h) in H.iteritems():
        cost += power(h)

    max_power = 0
    while Budget - cost >= p_min:
        max_charger = None

        # current chosen sets
        temp_c = []
        temp_h = []
        for (c, h) in H.iteritems():
            temp_c.append(c)
            temp_h.append(h)

        for c in chargers:
            if H.get(c, 0) < h_max:
                temp_Q = total_power(sensors, p_list, temp_c + [c], temp_h + [1])
                if temp_Q > max_power:
                    max_power = temp_Q
                    max_charger = c

        if max_charger != None:
            cost += p_min
            H[max_charger] = H.get(max_charger, 0) + 1
        else:
            if DEBUG:
                print 'Warning: remaining budget can not be full filled.'
            break

    if DEBUG:
        print "============================================="
        print "#       utilize the remaining budget        #"
        print "============================================="
        print 'Budget : %f' % cost

    result_c = []
    result_h = []
    for (c, h) in H.iteritems():
        result_c.append(c)
        result_h.append(h)

    result = (total_power(sensors, p_list, result_c, result_h), result_c, result_h)
    return result


def solution(chargers, sensors, p_list):
    """solution B body function"""
    return TCBalgorithm(chargers, sensors, p_list)
