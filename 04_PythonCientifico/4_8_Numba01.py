

from numba import jit
from numpy import arange

import time

def crono(f):
    """
    Regresa el tiempo que toma en ejecutarse la funcion.
    """
    def tiempo(x):
        t1 = time.time()
        f(x)
        t2 = time.time()
        return 'Elapsed time: ' + str((t2 - t1)) + "\n"
    return tiempo

# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.

@crono
#@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = arange(10000).reshape(100,100)
print(sum2d(a))

