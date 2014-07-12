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
    pprint(chargers)

    # step 2: generate sensors
    sensors = distributions['sensor']()
    print "============================================="
    print "#                 sensors                   #"
    print "============================================="
    pprint(sensors)

    # step 3: apply solution in config.py
    solution(chargers, sensors, p_list)

if __name__ == '__main__':
    main()
