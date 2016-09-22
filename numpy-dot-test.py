import numpy as np
import time

def dot_list(a, b):
    N = min(len(a), len(b))
    dot = 0
    for i in range(N):
        dot += a[i]*b[i]
    return dot

def dot_arr_for(a, b):
    N = min(a.shape[0], b.shape[0])
    dot = 0
    for i in range(N):
        dot += a[i]*b[i]
    return dot

def dot_arr(a, b):
    return (a*b).sum()

N = 10000000
list_a = list(range(N))
arr_a = np.arange(N)

t1 = time.time()
dot1 = dot_list(list_a, list_a)
t2 = time.time()
dot2 = dot_arr_for(arr_a, arr_a)
t3 = time.time()
dot3 = dot_arr(arr_a, arr_a)
t4 = time.time()

print(dot1, t2-t1)
print(dot2, t3-t2)
print(dot3, t4-t3)
