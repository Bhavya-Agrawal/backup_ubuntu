#!/usr/bin/python3
import time
import matplotlib.pyplot as plt

x = [2,3,4]
y = [8,9,0]

plt.scatter(x,y)
plt.show()
#time.sleep(2)
#plt.clf()

for i in range(5):
	fig = plot_figure()
	fig.clf()

print(plt.getfignums())


