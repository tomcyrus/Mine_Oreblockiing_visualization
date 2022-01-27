# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np

# '''
# def get_test_data(delta=0.05):

#     from matplotlib.mlab import  bivariate_normal
#     x = y = np.arange(-3.0, 3.0, delta)
#     X, Y = np.meshgrid(x, y)

#     Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
#     Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
#     Z = Z2 - Z1

#     X = X * 10
#     Y = Y * 10
#     Z = Z * 500
#     return X, Y, Z

# # '''


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x, y, z = axes3d.get_test_data(0.05)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2)

# plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np

# x = [1000,1000,1000,1000,1000,5000,5000,5000,5000,5000,10000,10000,10000,10000,10000]
# y = [13,21,29,37,45,13,21,29,37,45,13,21,29,37,45]
# z = [75.2,79.21,80.02,81.2,81.62,84.79,87.38,87.9,88.54,88.56,88.34,89.66,90.11,90.79,90.87]
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
# plt.show()



# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt



# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x =[1,2,3,4,5,6,7,8,9,10]
# y =[5,6,2,3,13,4,1,2,4,8]
# z =[2,3,3,3,5,7,9,11,9,10]



# ax.scatter(x, y, z, c='r', marker='o')

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
# import seaborn as sns


df=pd.read_csv('oreblock01.csv')
x = df['Easting']
y = df['Northing']
z = df['Grade']

fig=plt.figure(figsize=(8,6))
ax = fig.add_subplot( projection='3d')
# plt.figure(figsize=(8,6))
# plt.figure()
# ax = plt.axes( projection='3d')



n=float(input('enter cut off grade::'))
ax.scatter3D(x,y,df['Grade']>=n, c='r', marker='s', s=25)
# ax.plot_trisurf(x,y,df['Grade']>=n)

plt.show()

