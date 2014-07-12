# -*- coding: utf-8 -*-

from pprint import pprint
from common.function import total_power, power
from config import args

def charger_h(c, sensors, p_list):
    """calulate h for charger c(x, y) independently"""
    (ratio, h) = max([(total_power(sensors, p_list, [c], [h])/power(h), h) for h in xrange(args['h_max'] + 1)])
    return h

def power_levels(chargers, sensors, p_list):
    """return a list of h"""
    return [charger_h(c, sensors, p_list) for c in chargers];

def solution(chargers, sensors, p_list):
    """solution A body funciton"""
    # step 1: optimal power levels of all chargers
    h_list = power_levels(chargers, sensors, p_list)
    print "============================================="
    print "#           optimal power levels            #"
    print "============================================="
    pprint(h_list)

    # step 2: apply algorithm 3
