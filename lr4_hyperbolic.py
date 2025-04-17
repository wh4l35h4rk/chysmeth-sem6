import numpy as np
import matplotlib.pyplot as plt


def g(x, t):
    return t * x**2 * (1 - x)

def fi(x): # u(x, 0)
    return x * (1 - x)

def psi(x): # u_t(x, 0)
    return x**3 - x**2

def gamma0(t): # u(0, t)
    return 0

def gamma1(t): # u(l, t)
    return 0


if __name__ == '__main__':
    n = 10

    h = 1 / n
    tau = 0.01
    T = 0.5

    a = 1
    r = a**2 * tau**2 / h**2

    x = np.linspace(h, 1, n + 1)
    t = np.arange(tau, T, tau)

    M = len(x)
    N = len(t)


    u = np.zeros((M, N))

    for i in range(0, M):
        u[i][0] = fi(x[i])

    for i in range(0, M - 1):
        #  u[i][1] = psi(x[i]) * tau + u[i][0]
        u[i][1] = u[i][0] + (tau**2 / 2) * (a**2 / h**2 * (u[i - 1][0] - 2 * u[i][0] + u[i + 1][0]) + gamma0(t[i])) + tau * psi(x[i])

    for j in range(1, N):
        u[0][j] = gamma0(t[j])
        u[M - 1][j] = gamma1(t[j])


    for j in range(1, N - 1):
        for i in range(1, M - 1):
            u[i][j + 1] = 2 * u[i][j] - u[i][j - 1] + r * (u[i - 1][j] - 2 * u[i][j] + u[i + 1][j]) + tau**2 * g(x[i], t[j])

    print(u)

    X, T = np.meshgrid(x, t)

    plt.figure(figsize=(6, 5))
    plt.contourf(X, T, u.T, levels=20, cmap="plasma")
    plt.colorbar(label="Температура u(x,t)")
    plt.xlabel("x")
    plt.ylabel("t")

    plt.show()

