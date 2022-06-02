import math
import numpy as np
import pandas as pd

x0 = 1.5
for i in range(10):
    print(i+1,' ',1.0/pow(x0-1,1/2))
    x0 = 1.0/pow(x0-1,1/2)                                                                                                                                 