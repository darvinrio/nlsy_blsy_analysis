import numpy as np

# n1 = 2685
# n2 = 2685

n1 = 2468
n2 = 675

cAlpha = 1.95

dCrit = cAlpha*np.sqrt((n1+n2)/(n1*n2))

print(dCrit)