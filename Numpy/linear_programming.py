import numpy as np
import matplotlib.pyplot as plt

## Input ranges, counts ##
nrandom = 100000
min_x, max_x = 25, 200
min_y, max_y = 10, 100
## End ##

x = min_x + np.random.random(nrandom) * (max_x - min_x)  # n random numbers between max/min
y = min_y + np.random.random(nrandom) * (max_y - min_y)  # n random numbers between max/min

###### Put your functions in array below. As many as you like! ######
lp_functions = [
    np.where(10*x - 13*y > 100, True, False),
    np.where(2*x + 3*y < 500, True, False),
    np.where(-x + 10*y > 400, True, False),
    np.where(x > 100, True, False)
    ]
###### End ######

# plot each function
for f in lp_functions:
    plt.scatter(x[f], y[f], s=2, alpha=.1)
# plot intersection area
f = np.product(lp_functions, axis=0) > 0  # product represents AND condition
plt.scatter(x[f], y[f], s=2, c="blue", alpha=.75)
plt.show()
