# -*- coding: utf-8 -*-

from config import args, distributions, DEBUG, config_name
from common.function import func_D
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(chargers, sensors, anser):
    fig = plt.figure(figsize = (5, 5))
    ax = fig.add_subplot(111)

    (x, y) = args['size']

    # border
    ax.axis([0, x, 0, y])
    ax.set_xlabel('X(m)')
    ax.set_ylabel('Y(m)')
    ax.grid(True)

    # sensors & candidate chargers
    sensors_x = [x for (sid, x, y) in sensors]
    sensors_y = [y for (sid, x, y) in sensors]
    chargers_x = [x for (cid, x, y) in chargers]
    chargers_y = [y for (cid, x, y) in chargers]
    (plt_sensors, plt_chargers) = ax.plot(sensors_x, sensors_y, 'bo',
                                          chargers_x, chargers_y, 'r+',)

    plt_chargers.set_label('locations')
    plt_chargers.set_markeredgewidth(1.5)
    plt_sensors.set_label('devices')

    # legend
    leg = ax.legend(loc = 'best', numpoints = 1)
    leg.get_frame().set_alpha(0.75)

    (Q, C, H) = anser
    for (cid, x, y), h in zip(C, H):
        d = func_D(h)
        circ = patches.Circle((x, y), d, facecolor = 'yellow', alpha = 0.5)
        ax.add_patch(circ)

    # show plot
    plt.show()
