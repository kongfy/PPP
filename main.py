# -*- coding: utf-8 -*-

from pprint import pprint
from config import args, distributions, solution

def main():
    print "============================================="
    print "#                  args                     #"
    print "============================================="
    pprint(args)

    # step 1: generate candidate chargers
    chargers = distributions['charger']()
    print "============================================="
    print "#            candidate chargers             #"
    print "============================================="
    print "%d chargers generated:" % (len(chargers))
    pprint(chargers)

    # step 2: generate sensors
    sensors = distributions['sensor']()
    print "============================================="
    print "#                 sensors                   #"
    print "============================================="
    print "%d sensors generated." % (len(sensors))
    pprint(sensors)

    # step 3: generate p_list
    p_list = distributions['p_list']()
    print "============================================="
    print "#                sensor's P                 #"
    print "============================================="
    print "%d sensor's P generated." % (len(p_list))
    pprint(p_list)

    # step 3: apply solution in config.py
    anser = solution(chargers, sensors, p_list)
    print "============================================="
    print "#                solution                   #"
    print "============================================="
    pprint(anser)

if __name__ == '__main__':
    main()
