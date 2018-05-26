
import numpy as np

a = np.array([[2,3,4,5]])
b = np.array([[4,5,6,7]])
d = np.array([[4,5,6,7]])

c = np.concatenate((a,b,d))
print(c)

'''list_data = [[[2,3],[4,5]]]
a = [[7,8],[9,0]]
b= [[0,1],[2,3]]
print(type(a))
list_data.append(a)
list_data.append(b)
print(list_data)'''
