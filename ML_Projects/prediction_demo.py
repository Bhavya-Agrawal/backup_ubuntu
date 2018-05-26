#! /usr/bin/python3

from sklearn import tree
import sys

# to take input from user
inn = sys.argv
# adding features for apple and orange
# 0 to denote smooth and 1 to show bumpy as here we can only pass float or int value element in part 1 of list is to denote weight in gms
features = [[110,0],[130,0],[150,1],[170,1]]

# corresponding output we need each corresponding to the feature list
output = [["Apple"],["Apple"],["Orange"],["Orange"]]

# to apply algo of tree
algo = tree.DecisionTreeClassifier()

#for training machine with data set
trained_set = algo.fit(features,output)

#as argv in the form of list [weight,texture]
weight = int(inn[1])	#as 0th element includes file name while passing command line arguments

texture = int(inn[2])

# to predict 
result = trained_set.predict([[weight,texture]])


print(result)


## if we again and again run program it can even change or fluctuate the result
