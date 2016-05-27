import numpy as np
import matplotlib.pyplot as plt
import math
import random


def test():
    n = 100000
    x = [math.sqrt(-2 * math.log(random.random(), 2)) * math.cos(2*math.pi*random.random()) for i in range(n)]
    plt.figure(1)
    plt.subplot(131)
    plt.hist(x, 20)
    average = np.mean(x)
    deviation = np.std(x)
    max_val = np.max(x)
    min_val = np.min(x)
    x1, f1 = plot_function1(x)
    x2, f2 = plot_function2(x, n)
    plt.subplot(132)
    plt.plot(x1[1:], f1)
    plt.subplot(133)
    plt.plot(x2, f2)

    print average
    print deviation
    print min_val
    print max_val


def plot_function1(x):
    h, x1 = np.histogram(x, bins=20, normed=True)
    dx = x1[1] - x1[0]
    f = np.cumsum(h) * dx
    return x1, f


def plot_function2(x, n):
    x1 = np.sort(x)
    f = np.array(range(n))/float(n)
    return x1, f

test()
plt.show()

