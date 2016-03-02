# -*- coding: utf-8 -*-

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from solution.solutionB import solution as TCA
from config import DEBUG
import copy
import random
from common.function import total_power

def cost(C, H, C_p, H_p):
    n_1 = len(C)
    n_2 = len(C_p)
    cost = 0

    for i in xrange(n_2):
        for j in xrange(n_1):
            if C_p[i] == C[j]:
                cost += abs(H_p[i] - H[j])
                break
        else:
            cost += H_p[i]

    for j in xrange(n_1):
        for i in xrange(n_2):
            if C_p[i] == C[j]:
                break
        else:
            cost += H[j]

    if DEBUG:
        print "# ********** COST ********** : %d #" % (cost)
    return cost

def solution(chargers, sensors, p_list, B, sensors_p, p_list_p, F):
    Q, C, H = TCA(chargers, sensors, p_list)
    Q_p, C_p, H_p = TCA(chargers, sensors_p, p_list_p)


    F = int(B * F)
    while cost(C, H, C_p, H_p) > F:
        if DEBUG:
            print "======================================"
            print "#        result of TCAs'             #"
            print "======================================"
            print C, H
            print C_p, H_p

        # op on h
        n_1 = len(C)
        n_2 = len(C_p)

        temp_i = None
        temp_max = 0

        # find index
        for i in xrange(n_2):
            for j in xrange(n_1):
                if C_p[i] == C[j]:
                    if H_p[i] > H[j]:
                        C_tt = copy.copy(C_p)
                        H_tt = copy.copy(H_p)
                        H_tt[i] -= 1
                        t = total_power(sensors_p, p_list_p, C_tt, H_tt)
                        if temp_i == None or t > temp_max:
                            temp_i = i
                            temp_max = t
                    break
            else:
                C_tt = copy.copy(C_p)
                H_tt = copy.copy(H_p)
                H_tt[i] -= 1
                t = total_power(sensors_p, p_list_p, C_tt, H_tt)
                if temp_i == None or t > temp_max:
                    temp_i = i
                    temp_max = t

        H_p[temp_i] -= 1
        if H_p[temp_i] == 0:
            C_p[temp_i: temp_i + 1] = []
            H_p[temp_i: temp_i + 1] = []

        # random select j
        count = 0
        for j in xrange(n_1):
            for i in xrange(n_2):
                if C_p[i] == C[j]:
                    if H_p[i] < H[j]:
                        count += 1
                    break
            else:
                count += 1

        assert count > 0
        count = random.randint(0, count - 1)
        temp_j = None

        for j in xrange(n_1):
            for i in xrange(n_2):
                if C_p[i] == C[j]:
                    if H_p[i] < H[j]:
                        if count == 0:
                            temp_j = j
                        count -= 1
                    break
            else:
                if count == 0:
                    temp_j = j
                count -= 1

        charger = C[temp_j]

        # increase H'[j]
        for i in xrange(n_2):
            if C_p[i] == charger:
                H_p[i] += 1
                break
        else:
            C_p.append(charger)
            H_p.append(1)

    Q_p = total_power(sensors_p, p_list_p, C_p, H_p)
    return (Q_p, C_p, H_p)
