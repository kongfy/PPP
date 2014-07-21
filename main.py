# -*- coding: utf-8 -*-

from pprint import pprint
from config import args, distributions, DEBUG, config_name
import solution
from multiprocessing import Pool

def worker():
    """worker function, used to create processing"""
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

    result = {}

    anser = solution.solutionA.solution(chargers, sensors, p_list)
    result['A'] = anser
    if DEBUG:
        print "============================================="
        print "#                solution A                 #"
        print "============================================="
        pprint(anser)

    anser = solution.solutionB.solution(chargers, sensors, p_list)
    result['B'] = anser
    if DEBUG:
        print "============================================="
        print "#                solution B                 #"
        print "============================================="
        pprint(anser)

    anser = solution.solutionRan.solution(chargers, sensors, p_list)
    result['Random'] = anser
    if DEBUG:
        print "============================================="
        print "#               solution Ran                #"
        print "============================================="
        pprint(anser)

    anser = solution.solutionOpt.solution(chargers, sensors, p_list)
    result['Opt'] = anser
    if DEBUG:
        print "============================================="
        print "#               solution Opt                #"
        print "============================================="
        pprint(anser)

    return result

def main():
    """main function."""
    pool = Pool(args['worker']);

    tasks = [pool.apply_async(worker) for i in xrange(args['times'])]

    pool.close()
    pool.join()

    results = [task.get() for task in tasks]

    final = {}
    for result in results:
        for (key, (Q, C, H)) in result.iteritems():
            final[key] = final.get(key, 0) + Q

    for (key, Q) in final.iteritems():
        final[key] = Q / len(results)

    pprint(args)
    pprint(results)
    pprint(final)

    f = open('summary.txt', 'a')
    f.write(config_name + ' : ' + str(final) + '\n')
    f.close()

if __name__ == '__main__':
    main()
