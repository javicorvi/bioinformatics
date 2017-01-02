import matplotlib.pyplot as plt
x=[1,2,3,4,5]
axis=[0, 6, 0, 1]
plt.plot(x, [[0.62,0.65,0.90],[0.62,0.65,0.3],[0.62,0.63,0.5],[0.62,0.67,0.45],[0.61,0.62,0.56]],'ro')
plt.axis(axis)
plt.ylabel('AUC')
plt.xlabel('NSUS')
plt.show()