
# coding: utf-8

# In[78]:


import matplotlib.pyplot as plt
import numpy as np


# In[79]:


x=[1,2,3,4]
y=[5,6,7,8]
x1=[2,3,4,5]
y1=[1,4,5,3]
plt.scatter(x,y,color='r',marker='*')
plt.scatter(x1,y1,color='g',marker='*')
point = [2,4]
plt.scatter(point[0],point[1],color='y',marker='*',s=100)
plt.show()


# In[80]:


from math import sqrt
distance_list_x = []
distance_list_x1 = []
distance_list = []


# In[81]:


for i in range(0,len(x)):
    d=sqrt(((point[0]-x[i])**2)+((point[1]-y[i])**2))
    distance_list_x.append(d)
    distance_list.append(d)
   # print(len(x))
    


# In[82]:


print(distance_list_x)
print(len(distance_list_x))


# In[83]:


d_min = min(distance_list_x)


# In[84]:


print(d_min)


# In[85]:


for i in range(0,len(x1)):
    d=sqrt((point[0]-x1[i])**2+(point[1]-y1[i])**2)
    distance_list_x1.append(d)
    distance_list.append(d)


# In[86]:


d_min = min(distance_list_x1)
#print(d_min)
k=3
min_list=[]
#distance_list.append(distance_list_x)
#distance_list.append(distance_list_x1)
print(distance_list)


# In[87]:


for i in range(0,3):
    d_min=min(distance_list)
    print(d_min)
    min_list.append(d_min)
    distance_list.remove(d_min)


# In[88]:


print(min_list)


# In[89]:


count_x=0
count_x1=0
for i in min_list:
    if i in distance_list_x:
        count_x+=1
    elif i in distance_list_x1:
        count_x1+=1        
        


# In[91]:


#count_x and count_x1 are actually counting no of variables of a set in a circle formed

if count_x>count_x1:
    print("predicted output is set 1")
else:
    print("predicted output is set 2")


# In[ ]:




