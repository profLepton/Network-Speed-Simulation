import random
import numpy as np
from speed_up import get_network_efficiency

def run_iterations(epochs=10, n=10, S=0, e=0.1):
    true_p = [round(random.random(), 2) for _ in range(n)]
    estimated_trust = [(0, []) * n]



    for _ in range(epochs):
        get_network_efficiency(true_p, S, e)




if __name__ == '__main__':
    run_iterations()