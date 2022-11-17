#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
a = np.matrix('1 0 0; 2 1 0; -3 2 1')
a_inv = np.linalg.inv(a)
print(a_inv)


# In[ ]:




