#!/usr/bin/env python
# coding: utf-8

# #04 Pemilihan kolom (columns selection) pada Data Frame bedasarkan tipe data

# Import Modules

# In[1]:


import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)


# In[2]:


n_rows = 5
n_cols = 2
cols = ['bil_pecahan', 'bil_bulat']

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                 columns=cols)
df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pd.util.testing.makeDateIndex(n_rows, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE')

df


# In[4]:


df.dtypes


# Memilih kolom bertipe data numerik

# In[5]:


df.select_dtypes(include='number')


# In[7]:


df.select_dtypes(include='float')


# In[6]:


df.select_dtypes(include='int')


# Memilih kolom bertipe data string

# In[8]:


df.select_dtypes(include='object')


# Memilih kolom bertipe data datetime

# In[9]:


df.select_dtypes(include='datetime')


# Memilih kolom dengan kombinasi tipe data

# In[10]:


df.select_dtypes(include=['number', 'object'])


# In[ ]:




