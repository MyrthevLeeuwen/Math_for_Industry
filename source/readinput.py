import numpy as np
# Binning all the data based on position:
import numpy as np
# Boundaries of bins:
xmin, xmax = 0, 100
ymin, ymax = 0, 100
xbins, ybins = 10, 10
xstep = (xmax - xmin) / xbins
ystep = (ymax - ymin) / ybins

# Generate random data
x = np.random.randint(xmin, xmax, size=100)
y = np.random.randint(ymin, ymax, size=100)

# Bin the data
bins = np.zeros((xbins, ybins))
for i in range(len(x)):
    xi = int((x[i] - xmin) // xstep)
    yi = int((y[i] - ymin) // ystep)
    bins[xi, yi] += 1
