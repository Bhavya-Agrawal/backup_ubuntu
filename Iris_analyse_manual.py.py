
# coding: utf-8

# In[25]:


from sklearn.datasets import load_iris
from sklearn import tree
#from sklearn.cross_validation import train_test_split


# In[26]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[48]:


#test_size indicates the size of data we want to give for training the machine 
iris = load_iris()
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.8)


# In[49]:


#known or expected output

print(test_target)


# In[50]:


clf = tree.DecisionTreeClassifier()
# input is in train_data and output is as per train_target
trained = clf.fit(train_data,train_target)


# In[51]:


#we need to predict output as per test_data so give it in predict function
predicted = trained.predict(test_data)


# In[52]:


#predicted output
print(predicted)


# In[53]:


# print percentage of accuracy
pct = accuracy_score(test_target,predicted)


# In[54]:


print(pct)

