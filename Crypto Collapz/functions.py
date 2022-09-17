import numpy as np 

def max421(x):
    a = max(4,x)
    while x!=1 :
        if (x % 2 == 0):
            x = x/2
        else :
            x = 3 * x + 1
            a = max(x,a)
    return int(a)
