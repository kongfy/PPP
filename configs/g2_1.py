# -*- coding: utf-8 -*-

# debug output switch
DEBUG = True

# program arguments
args = {
    'size'    : (300, 300),      # (width, height) of 2-D plane
    'N'       : 6,               # numbers of candidate location/chargers [50, 100]
    'M'       : 50,              # numbers of sensors [500, 2000]
    'B'       : 800,             # power budget [10000, 20000]
    'p_min'   : float(50),
    'h_max'   : 4,
    'p_th'    : float(0.01),
    'alpha'   : float(0.64),
    'beta'    : float(30),
    'sp_min'  : float(0.02),     # lower bound of sensor's P
    'sp_max'  : float(0.03),     # upper bound of sensor's P
    'times'   : 10,              # repeat times
    'worker'  : 10,              # numbers of worker process
}

# choose how the chargers & sensors distributed
import generate
distributions = {
    'charger' : generate.charger.rand,
    'sensor'  : generate.sensor.rand,
    'p_list'  : generate.p_list.rand,
}

config_name = 'N = 6'
