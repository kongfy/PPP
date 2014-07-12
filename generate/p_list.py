# -*- coding: utf-8 -*-

from config import args
import random

def rand():
    """randomly generate p_list"""
    m = args['M']
    return [random.uniform(args['sp_min'], args['sp_max']) for i in xrange(m)]
