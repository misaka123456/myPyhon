import numpy as np
import time
import math
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

n = [2 ** 2, 2 ** 3, 2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8, 2 ** 9, 2 ** 10, 2 ** 11, 2 ** 12]
time1 = []
time2 = []
time3 = []

a = []
b = []
for i in range(2 ** 12):
    aa = []
    bb = []
    for j in range(2 ** 12):
        aa.append(random.randint(0, 9))
        bb.append(random.randint(0, 9))
    a.append(aa)
    b.append(bb)


for n1 in n:
    print("--------------------------")
    for i3 in range(3):
        if i3 == 0:
            oldTime = time.time()
            c1 = []
            for i1 in range(n1):
                cc = []
                for j1 in range(n1):
                    sum = 0
                    for k1 in range(n1):
                        sum = sum + a[i1][k1] * b[k1][j1]
                    cc.append(sum)
                c1.append(cc)
            newTime = time.time()
            time1.append(newTime - oldTime)
        # [0.0, 0.0, 0.0019979476928710938, 0.009993314743041992, 0.08194899559020996, 0.640606164932251, 5.16082763671875, 43.74709868431091, 367.34685039520264, 2954.358227491379, 23246.402121067047]
        # if i3 == 1:
        #
        # # if i3 == 2:


print(time1)



