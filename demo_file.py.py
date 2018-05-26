
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

import numpy as np

x=[2,3]
y=[5,6]


# In[2]:


a=plt.plot(x,y)


# In[3]:


plt.plot(x,y,marker="*",label = "line")
#dir(plot)
plt.plot(x,y,linewidth = 4)
plt.legend()
plt.show()


# In[7]:


a = np.array([[2,3],[4,5]])
b = np.array([[5,6],[7,8]])
print(a)


# In[8]:


print(b)


# In[15]:


plt.plot(a,b,linewidth=4,label="line via array")
plt.legend()
plt.show()
plt.plot(a[0],b[0],label="line b/w first row elements",color ='y')


# In[16]:


plt.plot(a[1],b[1],color='g')

