#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = 0.15
y0 = -2.1
delta = 0.1

def f1(y):
    return math.sin (y + 1) + 1
def f2 (x):
    return -math.sin(x - 1) + 1.5

def iter (x,y,e):
    xn = x
    yn=y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn = f1(xn)
        n += 1
    print ("Simple iteration:")
    print ("x=", xn, "\ny=",yn,"\nThe amount of iteration = ",n)
iter(x0,y0,0.0001)


# In[ ]:





# In[ ]:




