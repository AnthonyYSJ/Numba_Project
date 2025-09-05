import numpy as np
import timeit
from numba import jit, int32
from functools import partial

@jit(int32(int32, int32), cache=True, nopython=True)
def add(x, y):
    # A somewhat trivial example
    return x + y

def add_2(x, y):
    return x + y


if __name__ == '__main__':
    add_time = timeit.timeit(partial(add, 1, 2), number=10000000)
    add_time_2 = timeit.timeit(partial(add_2, 1, 2), number=10000000)

    print(add_time, add_time_2)

