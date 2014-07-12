# -*- coding: utf-8 -*-

# debug output switch
DEBUG = True

# program arguments
args = {
    'size'    : (1000, 1000),    # (width, height) of 2-D plane
    'N'       : 50,              # numbers of candidate location/chargers [50, 100]
    'M'       : 500,             # numbers of sensors [500, 2000]
    'B'       : 10000,           # power budget [10000, 20000]
    'p_min'   : float(100),
    'p_max'   : float(500),
    'h_max'   : 8,
    'p_th'    : float(0.01),
    'alpha'   : float(0.64),
    'beta'    : float(30),
    'sp_min'  : float(0.1),      # lower bound of sensor's P
    'sp_max'  : float(0.2),      # upper bound of sensor's P
}

# choose the solution you want to try
import solution
solution = solution.solutionA.solution

# choose how the chargers & sensors distributed
import generate
distributions = {
    'charger' : generate.charger.rand,
    'sensor'  : generate.sensor.rand,
    'p_list'  : generate.p_list.rand,
}
