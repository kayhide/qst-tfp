from functools import reduce, partial
import matplotlib.pyplot as plt
import numpy as np
import operator as op

la = np.linalg

verbose = False
quiet = False
if not verbose:
    def info(msg):
        pass
else:
    def info(msg):
        print(msg)

if quiet:
    def say(msg):
        pass
else:
    def say(msg):
        print(msg)

L = 1.
psi = lambda n, x: np.sqrt(2. / L) * np.sin(np.pi / L * x * int((n + 1) / 2))
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
