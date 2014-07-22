# -*- coding: utf-8 -*-

from pprint import pprint
from config import args, distributions, DEBUG, config_name
import solution
from multiprocessing import Pool
import timeit

def worker():
    tic = timeit.default_timer()
    
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

    """
    anser = solution.solutionOpt.solution(chargers, sensors, p_list)
    result['Opt'] = anser
    if DEBUG:
        print "============================================="
        print "#               solution Opt                #"
        print "============================================="
        pprint(anser)
    """
    toc = timeit.default_timer()
    return (toc - tic, result)

def main():
    """main function."""
    pool = Pool(args['worker']);

    tasks = [pool.apply_async(worker) for i in xrange(args['times'])]

    pool.close()
    pool.join()

    results = [task.get() for task in tasks]

    final = {}
    times = []
    for (time, result) in results:
        times.append(time)
        for (key, (Q, C, H)) in result.iteritems():
            value = final.get(key, {})
            value['max'] = max(value.get('max', 0), Q)
            value['min'] = min(value.get('min', float('inf')), Q)
            value['avg'] = value.get('avg', 0) + Q
            final[key] = value

    for (key, value) in final.iteritems():
        value['avg'] = value['avg'] / len(results)

    pprint(args)
    pprint(results)
    pprint(times)
    pprint(final)

    f = open('summary.txt', 'a')
    time_str = ' average time : %f s' % (sum(times) / len(times))
    f.write(config_name + ' : ' + str(final) + time_str + '\n')
    f.close()

if __name__ == '__main__':
    main()
