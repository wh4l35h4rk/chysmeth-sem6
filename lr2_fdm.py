import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

N = 100
h = 1 / N


def p(x):
    return x + 1

def q(x):
    return 1

def f(x):
    return -2 / (x + 1)**3

def star(x):
    return x / (x + 1)


def a(x):
    r = p(x) / 2 * h
    return (1 / h** 2) * (1 + abs(r) - np.sin(abs(r)) / (np.sin(abs(r)) + 1) - r)

def b(x, a_el, c_el):
    return q(x) - a_el - c_el

def c(x):
    r = p(x) / 2 * h
    return (1 / h ** 2) * (1 + abs(r) - np.sin(abs(r)) / (np.sin(abs(r)) + 1) + r)

def print_table(x, y, y_star):
    size = x.shape[0]
    table = PrettyTable()
    table.field_names = ["x", "y", "y*", "погрешность"]
    table.add_rows(
        [[x[i], y[i], y_star[i], abs(y_star[i] - y[i])] for i in range(size)]
    )
    print(table, '\n')



if __name__ == '__main__':
    alpha_0 = 0
    beta_0 = 1
    gamma_0 = 1

    alpha_1 = 1
    beta_1 = 0
    gamma_1 = 0.5

    x = np.array([i * h for i in range(N + 1)])
    f_arr = np.array([f(e) for e in x])

    A = np.zeros((N + 1, N + 1))

    for i in range(1, N):
        A[i][i - 1] = a(x[i])
        A[i][i] = b(x[i], a(x[i]), c(x[i]))
        A[i][i + 1] = c(x[i])

    # левое граничное условие
    if beta_0 == 0:
        A[0, 0] = alpha_0
        f_arr[0] = gamma_0
    else:
        A[0, 0] = -3 / (2 * h)
        A[0, 1] = 4 / (2 * h)
        A[1, 0] = -1 / (2 * h)
        f_arr[0] = gamma_0 / beta_0

    # правое граничное условие
    if beta_1 == 0:
        A[N, N] = alpha_1
        f_arr[N] = gamma_1
    else:
        A[N, N] = 3 / (2 * h)
        A[N, N - 1] = -4 / (2 * h)
        A[N, N - 2] = 1 / (2 * h)
        f_arr[N] = gamma_1 / beta_1


    y = np.linalg.solve(A, f_arr)

    y_star = [star(e) for e in x]

    print_table(x, y, y_star)

    plt.plot(x, y, label="численное решение", linestyle="--")
    plt.plot(x, y_star, label="точное решение")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()