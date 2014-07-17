# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power
from config import args, DEBUG
import random

def random_h():
    """generate a random h list"""
    B = args['B']
    cost = 0
    h_list = [0 for i in xrange(args['N'])]

    for i in xrange(len(h_list)):
        if cost >= B:
            break

        if cost + power(args['h_max']) <= B:
            h_list[i] = random.randint(0, args['h_max'])
        else:
            for h in xrange(args['h_max'] + 1):
                if cost + power(h) <= B:
                    h_list[i] = h

        cost += power(h_list[i])

    random.shuffle(h_list)
    return h_list

def random_solution(chargers, sensors, p_list):
    """get a random solution, return (Q, C, H)"""
    h_list = random_h();
    if DEBUG:
        print "============================================="
        print "#               random h list               #"
        print "============================================="
        pprint(h_list)

    C = []
    H = []

    for i in xrange(len(h_list)):
        if h_list[i] > 0:
            C.append(chargers[i])
            H.append(h_list[i])

    Q = total_power(sensors, p_list, C, H)

    return (Q, C, H)


def solution(chargers, sensors, p_list):
    """
    solution random body function.
    """
    return random_solution(chargers, sensors, p_list)
