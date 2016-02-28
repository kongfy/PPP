# -*- coding: utf-8 -*-

from config import args
import random

def reconfig(p_list, generator, leave = 0, enter = 0):
    """reconfiguration for sensors"""
    assert leave >= 0
    assert leave <= 1
    assert enter >= 0
    assert enter <= 1

    m = args['M']

    l = int(leave * m)
    e = int(enter * m)
    current = len(p_list)

    if current < l:
        return p_list

    p_list = p_list[l:]

    temp = generator() # TODO : rand_path() rand_trace() do not make sence here
    p_list += temp[:e]

    return p_list

def rand():
    """randomly generate p_list"""
    m = args['M']
    return [random.uniform(args['sp_min'], args['sp_max']) for i in xrange(m)]
