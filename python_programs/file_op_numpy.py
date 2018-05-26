from io import StringIO
import numpy as np
c = StringIO("0 1\n2 3")
y=np.loadtxt(c)
print(y)
