
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import matplotlib.image as img

image=img.imread('/home/bhavyaagrawal/Downloads/profile.jpg')
imgplot = plt.imshow(image)


# In[4]:


from sklearn.datasets import load_digits
digit = load_digits()
dir(digit)


# In[6]:


data = digit.data
print(data.shape)


# In[9]:


#to plot image corresponding to 1st data of digit

x = data[0].reshape(8,8)
print(x)


# In[10]:


plt.imshow(x)


# In[13]:


#to plot image corresponding to 8th data of digit in 2D array form of size (8*8) actually its size is (1*64) ie 1D

y = data[8].reshape(8,8)
print(y)
plt.imshow(y)


# In[15]:


# TO CHECK THE OUTPUT VALUE CORRESPONDING TO 5TH DATA 
print(digit.target[5])

