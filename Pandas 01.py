#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#01: Menyertakan Prefix dan Suffix pada seluruh kolom Data Frame


# In[2]:


import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)


# Persiapan Data Frame

# In[2]:


import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                 columns=cols)
df


# In[3]:


tuple('ABCDE')


# Menyertakan Prefix Kolom

# In[7]:


import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                 columns=cols)
df

df.add_prefix('kolom_')


# Menyertakan Suffix Kolom

# In[8]:


import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                 columns=cols)
df

df.add_suffix('_field')


# In[ ]:




