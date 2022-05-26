#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 00:38:24 2021

@author: davka
"""

import numpy as np
from data_handling import make_reflectivity_curves
import matplotlib.pyplot as plt




q_values = np.linspace(0.01, 0.14, 1024)
#test_data = np.loadtxt('dip.txt')  # in 1/m q =
q_values = q_values * 1e10 #I don't know why, but taken from orifinal script
print(q_values)

n_samples = 1
training_data_output = np.zeros([len(q_values), 1])

for x in range (1,128):
    
    grow = x*1e-10

    thickness = np.array([10e-10 + grow, 0, 0])
    repetitions = n_samples
    thicknesses = np.tile(thickness, (repetitions, 1))
#print(thicknesses)

    roughness = np.array([1e-10, 0e-10, 0e-10])
    repetitions = n_samples
    roughnesses = np.tile(roughness, (repetitions, 1))
#print(roughnesses)

    SLD = np.array([20e+14, 0e+14, 0e+14])
    repetitions = n_samples
    SLDs = np.tile(SLD, (repetitions, 1))
#print(SLDs)

    training_reflectivity = make_reflectivity_curves(
        q_values, thicknesses, roughnesses, SLDs, n_samples)



    labels = np.append(thickness, roughness)
    labels = np.append(labels, SLD)
    
    training_data_output = np.append(training_data_output, training_reflectivity, axis=1)
plt.plot(q_values, training_data_output[:,60])


import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


#plt.show()

#3D PLOT

# Create figure and add axis
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111, projection='3d')

# Remove gray panes and axis grid
ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.grid(False)# Remove z-axis
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])

print(training_data_output.shape)

# Create meshgrid
X, Y = np.meshgrid(np.linspace(10, 138, 128), np.linspace(0.02, 0.14, 1024))


training_data_output = np.log(training_data_output)
training_data_output = (training_data_output + 20) / 20


# Plot surface
plot = ax.plot_surface(X=X, Y=Y, Z=training_data_output, cmap='YlGnBu_r', vmin=0, vmax=1)
ax.set_xlabel('Thickness (A)')
ax.set_ylabel('q (1/nm)')
ax.set_zlabel('Reflectivity (log)')
plt.show()

































