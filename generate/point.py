# -*- coding: utf-8 -*-

import random

def random_point(width, height):
    """generate a random point in the given range"""
    return (random.randint(0, width), random.randint(0, height))
