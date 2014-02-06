from mpmath import mpf, mp

mp.dps = 600
print("Precision:", mp.prec)
def vectorize(functions):
    """
    Takes a list of functions and returns a function that accepts a list of
    values and applies each function given to the list of values.
    """
    def _vectorized(x, ys):
        return tuple(f(x, *ys) for f in functions)

    return _vectorized

def inc_vec(vec, inc):
    return [x + inc for x in vec]

def add_vec(*vecs):
    return [sum(nums) for nums in zip(*vecs)]

def mul_vec(vec, mul):
    return [x * mul for x in vec]

def rk4_system(y, x0, y0, h, steps):
    """
    y: list of ODE
    y0: vector (tuple) of initial y values
    Finds y(x0 + h * steps)
    """

    x1 = x0
    y1 = list(y0)
    xs = [x0]
    ys = [[y0[i]] for i,f in enumerate(y)]

    f = vectorize(y)

    for i in range(steps):
        k1 = f(x1, y1)
        k2 = f(x1 + (h / 2), add_vec(y1, mul_vec(k1, h / 2)))
        k3 = f(x1 + (h / 2), add_vec(y1, mul_vec(k2, h / 2)))
        k4 = f(x1 + h, add_vec(y1, mul_vec(k3, h)))

        y1 = add_vec(y1, mul_vec(add_vec(k1, mul_vec(k2, 2), mul_vec(k3, 2), k4), h / 6))
        for i, val in enumerate(y1):
            ys[i].append(val)
        x1 += h
        xs.append(x1)

    return xs, ys

if __name__ == '__main__':
    a1 = mpf('2')
    a2 = mpf('2')
    a3 = mpf('3')
    a4 = mpf('0.7')
    a5 = mpf('1')
    a6 = mpf('0.02')
    a7 = mpf('20')
    a8 = mpf('1')
    a9 = mpf('1')
    a10 = mpf('1')
    a11 = mpf('0.01')
    a12 = mpf('0.1')
    a13 = mpf('0.3')
    a14 = mpf('50')
    a16 = mpf('0.1')
    a17 = mpf('0.14')
    B = mpf('1')
    f1 = lambda p: p**a1 / (a2**a1 + p**a1)
    f2 = lambda p: a4 * a5**a3 / (a5**a3 + p**a3)
    p = lambda E, a15: (a14 * E * B) / a15
    d_a15 = mpf('0.015')
    y = [
        lambda t, A, M, E, a15: f1(p(E,a15))*(a6+a7*M)-a8*A-a9*A**2, #dA/dt
        lambda t, A, M, E, a15: a10*f2(p(E,a15))*A-f1(p(E,a15))*a16*a7*M-a11*M, #dM/dt
        lambda t, A, M, E, a15: a12*(1-f2(p(E,a15)))*A-a13*E, #dE/dt,
        None #da15/dt, which depends on parameter range
    ]

    import csv

    par_ranges = [
        # name,                 file,           initial,        da15/dt,                steps
        ("0.1 to 2",            "12",           mpf('0.1'),     mpf('0.0095'),          4000),
        ("2 to 0.1",            "21",           mpf('2'),       mpf('-0.0095'),         4000),
        ("0.5 to 2.3",          "0523",         mpf('0.5'),     mpf('0.009'),           4000),
        ("0.1 to 2 (Long)",     "12_long",      mpf('0.1'),     mpf('0.00316666667'),   20000),
    ]
    for par_range, file_suffix, initial, speed, steps in par_ranges:
        print("Running parameter range {}".format(par_range))
        print("\tInitial a15:", initial, "da15/dt:", speed)
        y[3] = lambda t, A, M, E, a15: speed # da15/dt
        xs, ys = rk4_system(y, mpf('0'), (mpf('0.5'), mpf('0'), mpf('1'), initial), mpf('0.05'), steps)
        with open('time_py_{}.dat'.format(file_suffix), 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for t, A, M, E, a15 in zip(xs, *ys):
                # TODO: use string formatting to avoid conversion issues
                writer.writerow([t, float(A), float(M), float(E), float(a15)])

    print("Finished")
