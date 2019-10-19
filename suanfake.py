import numpy as np
import time
import math
import random
import matplotlib as mpl
import matplotlib.pyplot as plt


x = 2
n = [10, 50, 100, 150, 200, 300, 400, 500, 10000, 20000, 50000, 100000]
a = []
time1 = []
time2 = []
time3 = []
time4 = []

for n100000 in range(100000):
    a.append(random.randint(0, 9))

for n1 in n:
    print("--------------------------")
    for i4 in range(4):
        if i4 == 0:
            #算法一
            oldTime = time.time()
            a1 = a[n1 - 1::-1]

            p1 = np.poly1d(a1)
            sum1 = p1(x)
            newTime = time.time()
            time1.append(newTime - oldTime)
            print(sum1)

        if i4 == 1:
            #算法二
            oldTime = time.time()
            sum2 = 0
            for i in range(n1):
                sum2 = sum2 + a[i] * x ** i
            newTime = time.time()
            time2.append(newTime - oldTime)
            print(sum2)

        if i4 == 2:
            #算法三
            oldTime = time.time()
            p3 = a[0]
            q3 = 1
            for i in range(1, n1):
                q3 = q3 * x
                p3 = p3 + a[i] * q3
            newTime = time.time()
            time3.append(newTime - oldTime)
            print(p3)

        # if i4 == 3:
        #     #算法四
            oldTime = time.time()
            p4 = a[n1 - 1]
            for i in range(n1 - 2, -1, -1):
                p4 = p4 * x + a[i]
            newTime = time.time()
            time4.append(newTime - oldTime)
            print(p4)
print("---------------------------")
print(time1)
print(time2)
print(time3)
print(time4)

plt.figure(figsize=(7, 8))
plt.subplot(411)
plt.plot(time1, 'b', lw=1.5, label='suanfa1')
plt.plot(time1, 'ro')
plt.legend(loc=0)
plt.title('suanfa1')
plt.xlabel('guimo')
plt.ylabel('shijian')
plt.grid(True)
plt.subplot(412)
plt.plot(time2, 'b', lw=1.5, label='suanfa2')
plt.plot(time2, 'ro')
plt.legend(loc=0)
plt.title('suanfa2')
plt.xlabel('guimo')
plt.ylabel('shijian')
plt.grid(True)
plt.subplot(413)
plt.plot(time3, 'b', lw=1.5, label='suanfa3')
plt.plot(time3, 'ro')
plt.legend(loc=0)
plt.title('suanfa3')
plt.xlabel('guimo')
plt.ylabel('shijian')
plt.grid(True)
plt.subplot(414)
plt.plot(time4, 'b', lw=1.5, label='suanfa4')
plt.plot(time4, 'ro')
plt.legend(loc=0)
plt.title('suanfa4')
plt.xlabel('guimo')
plt.ylabel('shijian')
plt.grid(True)
plt.show()

tt = []
tTime = []
for index in range(len(n)):
    tt = [time1[index], time2[index], time3[index], time4[index]]
    tTime.append(tt)
plt.plot(n, tTime, lw=1.5)
plt.plot(n, tTime, 'ro')
plt.xscale('log')
plt.grid(True)
plt.title('sizhong suanfa de shijian duibi tu')
plt.xlabel('guimo')
plt.ylabel('shijian')
plt.show()



