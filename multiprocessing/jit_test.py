# slow af (math = 1st, np = 2nd)
# takes around 0.8

import numpy as np
import time
from numba import jit

genotype = [1, 2, 3]

locs = np.array([(-10.0, 10.0), (10.0, 10.0), (10.0, -10.0), (-10.0, -10.0)])

@jit(nopython=True)
def measure_dist(gene, loc):
    tdist = 0
    tdist += np.linalg.norm(loc[0] - loc[1])
    for i in gene:
        if i < len(gene):
            tdist += np.linalg.norm(loc[i] - loc[i+1])
        else:
            tdist += np.linalg.norm(loc[i] - loc[0])
    print(tdist)

start = time.perf_counter()

measure_dist(genotype, locs)

end = time.perf_counter()
duration = end - start
print(duration)

