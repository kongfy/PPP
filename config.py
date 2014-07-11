# -*- coding: utf-8 -*-

args = {
    'size'    : (1000, 1000)     # (width, height) of 2-D plane
    'N'       : 50,              # numbers of candidate location/chargers [50, 100]
    'M'       : 500,             # numbers of sensors [500, 2000]
    'B'       : 10000,           # power budget [10000, 20000]
    'p_min'   : 100,
    'p_max'   : 500,
    'h_max'   : 8,
    'p_th'    : 0.01,
    'alpha'   : 0.64,
    'beta'    : 30,
}

distributions = {
    'chargers' : None,
    'sensors'  : None,
}
