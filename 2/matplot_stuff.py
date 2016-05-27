import numpy as np
import matplotlib.pyplot as plt

import math


def test():
    y = range(5)
    plt.plot(y)
    plt.title("Test $\pi$")
    plt.ylabel("This ist my label")
    plt.xlabel("this is sparta")
    plt.show()


def test2():
    t1 = [float(i)/10 for i in range(0, 50)]
    t2 = [float(i)/2000 for i in range(0, 10000)]
    ft1 = [math.exp(-t)*math.cos(2*math.pi*t) for t in t1]
    ft2 = [math.exp(-t)*math.cos(2*math.pi*t) for t in t2]

    plt.figure(1)
    plt.subplot(131)
    plt.plot(t1, ft1, 'bo', t2, ft2, 'k')

    plt.subplot(132)
    plt.plot(t2, ft2, 'r--')

    plt.subplot(133)
    plt.plot(t1, ft1, 'g-')


def test3():
    n = 100000
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(n)
    n, bins, patches = plt.hist(x, 50, facecolor="blue")
    print n
    print bins

if __name__ == "__main__":
    test3()
    plt.show()
