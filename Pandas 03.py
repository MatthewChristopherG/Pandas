#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#03 Konversi tipe data String ke Numerik pada kolom Data Frame


# Import Modules

# In[1]:


import pandas as pd

print(pd.__version__)


# Persiapan Data Frame

# In[4]:


data = {'col1':['1','2','3','teks'],
        'col2':['1','2','3','4']}
df = pd.DataFrame(data)
df


# In[5]:


df.dtypes


# In[6]:


df_x = df.astype({'col2':'int'})
df_x


# In[8]:


df_x.dtypes


# In[9]:


df_x = df.astype({'col2':'float'})
df_x


# In[10]:


df_x.dtypes


# Konversi tipe data numerik dengan fungsi to_numeric()

# In[11]:


df.apply(pd.to_numeric, errors='coerce')

