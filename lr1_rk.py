import numpy as np
from prettytable import PrettyTable

np.random.seed(3)
a = np.random.randint(50)
b = np.random.randint(50)
c = np.random.randint(50)

def check(x):
    if x == 0:
        return 0
    return a/b - ((c - x)**b * a) / (c**b * b)

def f(x, y):
    return (a - b * y) / (c - x)


def RK(f, x, y, h):
    for i in range(1, len(x)):
        Y1, Y2 = y[i - 1], y[i - 1]
        for _ in range(10):
            Y1_new = y[i - 1] + h * (1 / 4 * f(x[i - 1], Y1) - 1 / 4 * f(x[i - 1] + 2 / 3 * h, Y2))
            Y2_new = y[i - 1] + h * (1 / 4 * f(x[i - 1], Y1_new) + 5 / 12 * f(x[i - 1] + 2 / 3 * h, Y2))

            if max(abs(Y1_new - Y1), abs(Y2_new - Y2)) < 1e-4:
                break

            Y1, Y2 = Y1_new, Y2_new

        y[i] = y[i - 1] + h / 4 * (f(x[i - 1], Y1) + 3 * f(x[i - 1] + 2 / 3 * h, Y2))
    return y

def print_table(x, y, y_star):
    size = x.shape[0]
    table = PrettyTable()
    table.field_names = ["x", "y", "y*", "погрешность"]
    table.add_rows(
        [[x[i], y[i], y_star[i], abs(y_star[i] - y[i])] for i in range(size)]
    )
    print(table, '\n')



if __name__ == '__main__':
    h = 0.1
    x = np.array([i * h for i in range(0, int(1 / h) + 1)])
    y = np.zeros(len(x))

    y = RK(f, x, y, h)
    y_star = [check(e) for e in x]
    print_table(x, y, y_star)


    h = 0.05
    x = np.array([i * h for i in range(0, int(1 / h) + 1)])
    y = np.zeros(len(x))

    y = RK(f, x, y, h)
    y_star = [check(e) for e in x]
    print_table(x, y, y_star)
