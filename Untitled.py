
# coding: utf-8

# In[4]:


import numpy as np


# In[33]:


n = np.array([[21],[31]])
print(n.shape)


# In[34]:


n.astype(str)


# In[35]:


n.astype(int)


# In[36]:


np.array([])


# In[37]:


np.savetxt('a.txt',n)


# In[44]:


a=np.loadtxt('a.txt').astype(str)


# In[45]:


print(a)


# In[46]:


a=np.genfromtxt('a.txt',dtype=None)
## no change in the datatype ##


# In[47]:


print(a)

