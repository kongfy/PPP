# -*- coding: utf-8 -*-

import random

"""
generate a random point in the given range
"""
def random_point(width, height):
    return (random.randint(0, width), random.randint(0, height))
