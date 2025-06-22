import sympy as sym
import matplotlib


def g0():
    return 1

def g1():
    return sym.exp(1) + 1


if __name__ == '__main__':
    N = 20
    M = N - 2
    k = [i for i in range(N)]

    x = sym.Symbol('x')
    v = sym.symarray('v', M)

    a = 0
    b = 1
    h = (b - a) / N

    p = 1
    q = -1
    f = -x

    u_gran = g0() + (g1() - g0()) / (b - a) * (x - a)

    x_net = [a + i * h for i in range(0, N)]
    t = [(x - x_net[i]) / h for i in range(0, N)]

    phi_net = []
    for i in range(1, N - 1):
        phi = 1 - x ** (2 * k[i])
        phi_net.append(phi)

    u = sum([v[i] * phi_net[i] for i in range(0, M)])

    du2 = sym.diff(u, x, x)
    R = p * du2 + q * u + f

    system = [sym.integrate(phi_net[i] * R, (x, a, b)) for i in range(M)]
    true_v = sym.linsolve(system, tuple(v))

    solution = list(true_v)[0]
    func = sum([solution[i] * phi_net[i] for i in range(M)]) + u_gran

    plot = sym.plot(func, (x, a, b), label="Приближенное решение")
    p_star = sym.plot(x + sym.exp(x), (x, a, b), label="Точное решение")
    plot.append(p_star[0])
    plot.legend = True
    plot.show()
