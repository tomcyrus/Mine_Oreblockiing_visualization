
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib import cm


# ax = fig.gca( projection='3d')
# axes = plt.gca()
# plt.style.use('fivethirtyeight')

plt.rcParams['legend.fontsize'] = 6

fig=plt.figure(figsize=(8,6))
ax = plt.axes( projection='3d')
# ax = fig.add_subplot(111, projection='3d')

namafile = 'coords2.csv'
header1 = "Northing"
header2 = "Easting"
header3 = "Grade"

index = count()
n=float(input('enter cut off grade::'))

def animate(i):
    data = pd.read_csv('coords2.csv')
    x = data[header1] 
    y = data[header2]
    z = data[header3]
    print(z>n)

    ax.plot_trisurf(x, y,z, linewidth=0.05)

ani = FuncAnimation(plt.gcf(), animate, interval=6.4)

plt.tight_layout()
plt.title("linear interpolation")
plt.legend(labels=["Grade","Cut off Grade"],loc='lower right')  

plt.show()
