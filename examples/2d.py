import numpy
import matplotlib.pyplot as plt

# Set the L3 plot style
plt.style.use("style/l3.mplstyle")

# A power law model
def model(x):
    return 1E-04 + (1. - 1E-04) * (x / 90.)**3

# Sample the model
x0 = numpy.linspace(0., 90., 901)
y0 = model(x0)

# Sample random deviates from the model
sigma = 0.3
x1 = numpy.linspace(5., 65., 13)
n = len(x1)
y1 = model(x1) * (1. + sigma * numpy.random.randn(n))
dx1 = 1. + 3. * numpy.random.rand(n)
dy1 = model(x1) * sigma

# Plot the result
plt.figure()
plt.semilogy(x0, y0, "k-")
plt.errorbar(x1, y1, xerr=dx1, yerr=dy1, fmt="ko")
plt.xlabel(r"angle, $\alpha$ (deg)")
plt.xticks(numpy.linspace(0., 90., 7))
plt.ylabel(r"efficiency, $\epsilon$")
plt.axis((0., 90., 1E-04, 1.))
plt.legend(("expected", "measured"), loc=4)
plt.savefig("examples/2d.png")
plt.show()
