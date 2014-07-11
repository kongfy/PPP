# -*- coding: utf-8 -*-

from pprint import pprint
from config import *
import generate

def main():
    print "============================================="
    print "#                  args                     #"
    print "============================================="
    pprint(args)

    # step 1: generate candidate chargers
    chargers = distributions['charger']()
    print "============================================="
    print "#            condidate chargers             #"
    print "============================================="
    pprint(chargers)

    # setp 2: generate sensors
    sensors = distributions['sensor']()
    print "============================================="
    print "#                 sensors                   #"
    print "============================================="
    pprint(sensors)

    # step 3: apply solution in config.py


if __name__ == '__main__':
    main()
