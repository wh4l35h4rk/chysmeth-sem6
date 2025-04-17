import numpy as np
import matplotlib.pyplot as plt


def fi(x, t):
    return t * x * (1 - x)

def ksi(x):
    return x**2 - x

def gamma0(t):
    return 0

def gamma1(t):
    return 0


if __name__ == '__main__':
    n = 6

    h = 1 / n
    tau = 0.01
    T = 0.5

    a = 1
    r = a * tau / h ** 2

    x = np.linspace(h, 1, n + 1)
    t = np.arange(tau, T, tau)

    M = len(x)
    N = len(t)


    # ЯВНАЯ СХЕМА

    if a * tau / h ** 2 > 0.5:
        print("схема неустойчива!")


    u_exp = np.zeros((M, N))

    for i in range(M):
        u_exp[i][0] = ksi(x[i])

    for j in range(1, N):
        u_exp[0][j] = gamma0(t[j])
        u_exp[M - 1][j] = gamma1(t[j])


    for j in range(0, N - 1):
        for i in range(1, M - 1):
            u_exp[i][j + 1] = (r * (u_exp[i + 1][j] - 2 * u_exp[i][j] + u_exp[i - 1][j]) + u_exp[i][j] + tau * fi(x[i], t[j]))

    print(u_exp)


    # НЕЯВНАЯ СХЕМА

    A = np.zeros((M - 2, M - 2))

    for i in range(M - 2):
        if i > 0:
            A[i][i - 1] = -r
        A[i][i] = 1 + 2 * r
        if i < M - 3:
            A[i][i + 1] = -r

    u_imp = np.zeros((M, N))

    for i in range(M):
        u_imp[i][0] = ksi(x[i])

    for j in range(1, N):
        u_imp[0][j] = gamma0(t[j])
        u_imp[M - 1][j] = gamma1(t[j])

    for j in range(N - 1):
        B = u_imp[1:M - 1, j] + tau * fi(x[1:M - 1], t[j])
        B[0] += r * u_imp[0][j + 1]
        B[-1] += r * u_imp[M - 1][j + 1]

        u_imp[1:M - 1, j + 1] = np.linalg.solve(A, B)



    X, T = np.meshgrid(x, t)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.contourf(X, T, u_exp.T, levels=20, cmap="plasma")
    plt.colorbar(label="Температура u(x,t)")
    plt.xlabel("x")
    plt.ylabel("t")
    plt.title("Явная схема")

    plt.subplot(1, 2, 2)
    plt.contourf(X, T, u_imp.T, levels=20, cmap="plasma")
    plt.colorbar(label="Температура u(x,t)")
    plt.xlabel("x")
    plt.ylabel("t")
    plt.title("Неявная схема")

    plt.tight_layout()
    plt.show()

