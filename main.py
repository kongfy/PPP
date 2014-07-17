# -*- coding: utf-8 -*-

from pprint import pprint
from config import args, distributions, DEBUG
import solution

def main():
    if DEBUG:
        print "============================================="
        print "#                  args                     #"
        print "============================================="
        pprint(args)

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

    """
    anser = solution.solutionA.solution(chargers, sensors, p_list)
    print "============================================="
    print "#                solution A                 #"
    print "============================================="
    pprint(anser)

    anser = solution.solutionB.solution(chargers, sensors, p_list)
    print "============================================="
    print "#                solution B                 #"
    print "============================================="
    pprint(anser)
    """

    anser = solution.solutionRan.solution(chargers, sensors, p_list)
    print "============================================="
    print "#               solution Ran                #"
    print "============================================="
    pprint(anser)

    anser = solution.solutionOpt.solution(chargers, sensors, p_list)
    print "============================================="
    print "#               solution Opt                #"
    print "============================================="
    pprint(anser)

if __name__ == '__main__':
    main()
