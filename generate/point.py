# -*- coding: utf-8 -*-

import random

def random_point(width, height):
    """generate a random point in the given range"""
    return (random.uniform(0, width), random.uniform(0, height))

def add_point_to(points, pid, width, height):
    """add a random point to points"""
    point = random_point(width, height)
    while point in points:
        point = random_point(width, height)
    (x, y) = point
    points.append((pid, x, y))
