import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def corr(xs, ys):
    return cov(xs, ys) / (sigma(xs) * sigma(ys))


def cov(xs, ys):
    return E((xs - E(xs)) * (ys - E(ys)))


def E(xs):
    return np.mean(xs)


def sigma(xs):
    return np.std(xs)


def err(ys, yes):
    result = (ys - yes) ** 2
    return sum(result)


def test1(x, y1e, y2e):
    plt.figure(1)
    plt.plot(x, y1e, "r^")
    plt.plot(x, y2e, "bo")
    plt.axes([-0.1, 1.1, 0.5, 2.5])
    print corr(x, y1e)
    print corr(x, y2e)
    print np.corrcoef(x, y1e)[0][1]
    print np.corrcoef(x, y2e)[0][1]
    plt.show()


def test2():
    N = 50
    A = 2
    B = 3
    C = 2
    mu = 0
    sigma1 = 0.05
    x = np.linspace(0, 1, N)
    y1 = A + B * x
    y2 = C - B * x

    np.random.seed(0)
    e1 = np.random.normal(loc=mu, scale=sigma1, size=N)
    e2 = np.random.normal(loc=mu, scale=sigma1, size=N)

    y1e = y1 + e1
    y2e = y2 + e2
    #test1(x, y1e, y2e)

    fitlm = stats.linregress(x, y1e)
    print fitlm
    print fitlm.slope
    print fitlm.intercept
    print fitlm.rvalue

    plt.figure(1)
    plt.plot(x, y1e, "ro")
    plt.plot(x, fitlm.intercept + x * fitlm.slope, "b-")
    plt.show()


if __name__ == "__main__":
    N = 20
    A = 2
    B = 3
    C = 2
    mu = 0
    sigma1 = 0.05
    x = np.linspace(0, 5, N)
    y = A + B * x + C * x ** 2

    ye = y + np.random.normal(loc=0, scale=2.0, size=N)
    yf1 = np.polyval(np.polyfit(x, ye, 1), x)
    yf2 = np.polyval(np.polyfit(x, ye, 2), x)
    yfn = np.polyval(np.polyfit(x, ye, N), x)
    plt.figure(1)
    plt.plot(x, y, "g-")
    plt.plot(x, ye, "bo")
    plt.plot(x, yf1, "r-")
    plt.plot(x, yf2, "k-")
    plt.plot(x, yfn, "m-")
    plt.show()
    print err(y, yf1)
    print err(y, yf2)
    print err(y, yfn)
