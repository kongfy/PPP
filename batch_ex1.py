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

    # EXTENSION : reconfiguration
    G_sensors_p = []
    for i in xrange(args['times']):
        sensors_p = copy.copy(sensors)
        sensors_p = generate.sensor.reconfig(sensors_p, distributions['sensor'], args['leave'], args['enter'])
        if DEBUG:
            print "============================================="
            print "#                sensors'                   #"
            print "============================================="
            print "%d sensors' generated." % (len(sensors_p))
            pprint(sensors_p)
        G_sensors_p.append(sensors_p)


    G_p_list_p = []
    for i in xrange(args['times']):
        p_list_p = copy.copy(p_list)
        p_list_p = generate.p_list.reconfig(p_list_p, distributions['p_list'], args['leave'], args['enter'])
        if DEBUG:
            print "============================================="
            print "#                reconfig P                  #"
            print "============================================="
            print "%d sensor's P generated." % (len(p_list))
            pprint(p_list_p)
        G_p_list_p.append(p_list_p)

    for F in args['F']:
        extension1(0,
                   F,
                   copy.deepcopy(chargers),
                   copy.deepcopy(sensors),
                   copy.deepcopy(p_list),
                   copy.deepcopy(G_sensors_p),
                   copy.deepcopy(G_p_list_p),
        )

if __name__ == '__main__':
    main()
