import numpy as np


def p(x):
    return 1

def q(x):
    return -1

def f(x):
    return -x


def u0():
    return 1

def u1():
    return np.exp(1) + 1

def phi(x, k):
    return np.exp(x) + (k + 1)


if __name__ == '__main__':
    print(phi(0, 0), u0())
    print(phi(1, 0), u1())

