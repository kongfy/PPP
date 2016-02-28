# -*- coding: utf-8 -*-

from pprint import pprint
from config import args, distributions, DEBUG, config_name
import generate
import solution
import reconfiguration.iaa
from multiprocessing import Pool
import timeit
import copy

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

    # EXTENSION : reconfiguration
    sensors_p = copy.copy(sensors)
    sensors_p = generate.sensor.reconfig(sensors_p, distributions['sensor'], args['leave'], args['enter'])
    if DEBUG:
        print "============================================="
        print "#                sensors'                   #"
        print "============================================="
        print "%d sensors' generated." % (len(sensors_p))
        pprint(sensors_p)

    p_list_p = copy.copy(p_list)
    p_list_p = generate.p_list.reconfig(p_list_p, distributions['p_list'], args['leave'], args['enter'])
    if DEBUG:
        print "============================================="
        print "#                reconfig P                  #"
        print "============================================="
        print "%d sensor's P generated." % (len(p_list))
        pprint(p_list_p)

    result = {}

    tic = timeit.default_timer()
    anser = reconfiguration.iaa.solution(chargers, sensors, p_list, args['B'], sensors_p, p_list_p, args['F'])
    toc = timeit.default_timer()
    result['IAA'] = (toc - tic, anser)
    if DEBUG:
        print "============================================="
        print "#               solution IAA                #"
        print "============================================="
        pprint(anser)


    tic = timeit.default_timer()
    anser = solution.solutionOpt.solution(chargers, sensors_p, p_list_p)
    toc = timeit.default_timer()
    result['Opt'] = (toc - tic, anser)
    if DEBUG:
        print "============================================="
        print "#               solution Opt                #"
        print "============================================="
        pprint(anser)

    return result

def main():
    """main function."""
    pool = Pool(args['worker'])

    tasks = [pool.apply_async(worker) for i in xrange(args['times'])]

    pool.close()
    pool.join()

    results = [task.get() for task in tasks]

    final = {}
    times = []
    for result in results:
        for (key, (time, (Q, C, H))) in result.iteritems():
            value = final.get(key, {})
            value['time'] = value.get('time', 0) + time
            value['max'] = max(value.get('max', 0), Q)
            value['min'] = min(value.get('min', float('inf')), Q)
            value['avg'] = value.get('avg', 0) + Q
            final[key] = value

    for (key, value) in final.iteritems():
        value['time'] = value['time'] / len(results)
        value['avg'] = value['avg'] / len(results)

    pprint(args)
    pprint(results)
    pprint(times)
    pprint(final)

    f = open('summary.txt', 'a')
    f.write(config_name + ' : ' + str(final) + '\n')
    f.close()

if __name__ == '__main__':
    worker()
