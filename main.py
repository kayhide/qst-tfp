from functools import reduce, partial
import numpy as np
import matplotlib.pyplot as plt
import operator as op

verbose = False
quiet = False
if not verbose:
    info = lambda msg: nil
else:
    info = lambda msg: print(msg)

if quiet:
    say = lambda msg: nil
else:
    say = lambda msg: print(msg)

L = 1.0
psi = lambda n, x: np.sqrt(2.0 / L) * np.sin(np.pi / L * x * int((n + 1) / 2))
sumup = lambda f, n, x: reduce(op.add, (f(i, x) ** 2 for i in range(1, n + 1)), 0)


def plot(f, dst):
    fig, ax = plt.subplots()
    x = np.linspace(0, 1, 1024)
    y = [f(x) for x in x]
    ax.plot(x, y)
    plt.savefig(dst)
    say(f"create: {dst}")


for n in [2, 10, 100, 200]:
    f = partial(sumup, psi, n)
    dst = f"output/plot-{n}.png"
    plot(f, dst)
