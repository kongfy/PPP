# -*- coding: utf-8 -*-

from pprint import pprint
import os
import os.path
import shutil
from extension1 import extension1
from config import args, distributions, DEBUG, config_name
import generate

import copy

def configs():
    for root, dirs, files in os.walk('configs'):
        for filename in files:
            yield os.path.join(root, filename)

def main():
    config_filename = os.path.join(os.getcwd(), 'config.py')
    config_pyc = config_filename + 'c'
    result_dir = os.path.join(os.getcwd(), 'results')

    # step 1: generate candidate chargers
    chargers = distributions['charger']()
    if DEBUG:
        print "============================================="
        print "#            candidate chargers             #"
        print "============================================="
        print "%d chargers generated:" % (len(chargers))
        pprint(chargers)

    # step 2: generate sensors
    sensors = distributions['sensor']()
    if DEBUG:
        print "============================================="
        print "#                 sensors                   #"
        print "============================================="
        print "%d sensors generated." % (len(sensors))
        pprint(sensors)

    # step 3: generate p_list
    p_list = distributions['p_list']()
    if DEBUG:
        print "============================================="
        print "#                sensor's P                 #"
        print "============================================="
        print "%d sensor's P generated." % (len(p_list))
        pprint(p_list)

    for rate in args['rates']:
        extension1(rate,
                   args['F'],
                   copy.deepcopy(chargers),
                   copy.deepcopy(sensors),
                   copy.deepcopy(p_list),
                   None,
                   None,
        )

if __name__ == '__main__':
    main()
