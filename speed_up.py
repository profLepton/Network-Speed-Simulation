import random
import math

def get_m(x, e):
    if x == 1:
        return 1
    return math.ceil(math.log(e, 1-x))

def get_speed_up(nm_list, P):
    x_1 = 0
    for nm in nm_list:
        x_1 += nm[0]/nm[1]

    x = 1/ x_1
    speed_up = 1 / (1 + P * (x - 1))

    return speed_up

def get_network_efficiency(network_p_values, S=0, e=0.1):
    # Load on network is completely paralellizable
    # Acceptable failure rate (e) is 0.1 by default.
    P = 1 - S
    network_p_values.sort()

    nm_list = list(set([(p.count(x), get_m(x, e)) for x in network_p_values]))

    speed_up = get_speed_up(nm_list, P)

    return speed_up
