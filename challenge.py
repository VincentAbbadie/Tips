# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 05:35:22 2023

@author: M94089
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

fig, ax=plt.subplots()

#(x,y)
ax.plot([1,2,3,4],[1,4,2,3])

#fig = plt.figure()  # an empty figure with no Axes
#fig, ax = plt.subplots()  # a figure with a single Axes
#fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one axes on the left, and two on the right:
#fig, axs = plt.subplot_mosaic([['left', 'right_top'],['left', 'right_bottom']])

t=np.linspace(0,12,13)
r=np.linspace(0,4, 5)

print(f'{t=}')
print(f'{r=}')



nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
print(f'{x=}')
y = np.linspace(0, 1, ny)
print(f'{y=}')
xv, yv = np.meshgrid(x, y)
print(f'{xv=}')
print(f'{yv=}')
plt.plot(xv, yv, marker='o', color='k', linestyle='none')
plt.show()


X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma',
                          norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

data1, data2, data3 = np.random.randn(3, 100)  # make 3 random data set

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')