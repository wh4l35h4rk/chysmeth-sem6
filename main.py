import sympy as sym
import matplotlib


def g0():
    return 1

def g1():
    return sym.exp(1) + 1


def phi(x, k):
    return x * (1 - x) * x**k


if __name__ == '__main__':
    N = 8
    k = [i for i in range(N)]

    x = sym.Symbol('x')
    C = sym.symarray('C', N)

    a = 0
    b = 1

    p = 1
    q = -1
    f = -x

    u_gran = g0() + (g1() - g0()) / (b - a) * (x - a)

    u = sum([C[i] * phi(x, k[i]) for i in range(0, N)]) + u_gran
    print(u)

    diff_u = sym.diff(u, x)

    integral_func = (p * diff_u ** 2) - (q * u ** 2) - (2*f * u)
    J = sym.integrate(integral_func, (x, a, b))

    diff = [sym.diff(J, C[i]) for i in range(0, N)]

    true_C = sym.linsolve(diff, tuple(C))
    solution = list(true_C)[0]

    func = sum([solution[i] * phi(x, k[i]) for i in range(0, N)]) + u_gran

    p = sym.plot(func, (x, a, b), label="Приближенное решение")
    p_star = sym.plot(x + sym.exp(x), (x, a, b), label="Точное решение")
    p.append(p_star[0])
    p.legend = True
    p.show()
