#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#02: Pemilihan baris (rows selection) pada Data Frame


# In[1]:


import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)


# Persiapan Data Frame

# In[3]:


import pandas as pd
import numpy as np

n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 5, size=(n_rows, n_cols)),
                 columns=cols)
df


# Selection dengan operator logika |

# In[4]:


df[(df['A'] == 1) | (df['A'] == 3)]


# Selection dengan fungsi isin()

# In[5]:


df[df['A'].isin([1, 3])]


# Mengenal operator ~

# In[6]:


df[~df['A'].isin([1,3])]


# In[ ]:




