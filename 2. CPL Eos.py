#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:29:59 2024

@author: adam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams["mathtext.fontset"]="cm"
plt.rcParams['figure.figsize'] = 40, 12
cm_font = font_manager.FontProperties(fname="cmunrm.ttf")
#fonts = font_manager.findSystemFonts()
#ticks_font = font_manager.FontProperties(family='cm')
#%%Theoretical EoS
#Equation of state (w0 > -1, wa<0)
data = np.loadtxt("Documents/GitHub/CPL/output/CPL00_background.dat")
z = data[:,0]
a = 1/(1+z)
a=a[-1000:]
#a = np.linspace(0, 1., 1000)
w0 = np.array([-0.8, -0.6, -0.4, -0.2])
wa = np.array([-1.5, -1.5, -1.5, -1.5])
lines = len(w0)
ac = 1+ (1+w0)/wa


omega_mat = np.array([np.zeros(len(a))])
omega_mat_with_cross = np.array([np.zeros(len(a))])
for j in range(0 , lines):
    omega = np.array([np.zeros(len(a))])
    omega_with_cross = np.array([np.zeros(len(a))])
    for i in range(0, len(a)):
        if a[i] > ac[j]:
            omega[0,i] =  w0[j] + wa[j]*(1-a[i])
        else:
            omega[0,i] =  -1.
        omega_with_cross[0,i] = w0[j] + wa[j]*(1-a[i])
    omega_mat_with_cross = np.append(omega_mat_with_cross, omega_with_cross, axis = 0)
    omega_mat = np.append(omega_mat, omega, axis = 0)



fig = plt.figure(figsize = (16,5.5))
ax = fig.add_subplot(1,2,1)
for i in range(1,lines+1):
    ax.plot(a, omega_mat_with_cross[i],color = "C0",linestyle = "--", label = r"$\rm \omega$")
    ax.plot(a, omega_mat[i],color = "C1", label = r"$\rm \omega_{no_cross}$")

#ax.set_xlim(10**-3)

#ax.legend(fontsize = 13)
ax.set_xlabel("$a$", fontsize =20)
ax.set_ylabel(r"$\omega$", fontsize = 20)
ax.tick_params(axis='both', which='major', labelsize=15)

#%%Theoretical EoS
#Equation of state (wa>0)
data = np.loadtxt("Documents/GitHub/CPL/output/CPL00_background.dat")
z = data[:,0]
a = 1/(1+z)
a=a[-1000:]
#a = np.linspace(0, 1., 1000)
w0 = np.array([-1.6])
wa = np.array([-1.5])
lines = len(w0)
ac = np.array([])


omega_mat = np.array([np.zeros(len(a))])
omega_mat_with_cross = np.array([np.zeros(len(a))])
for j in range(0 , lines):
    if wa[j]!=0:
        ac = np.append(ac, 1+ (1+w0[j])/wa[j])
    else:
        ac = np.append(ac,-1)

    omega = np.array([np.zeros(len(a))])
    omega_with_cross = np.array([np.zeros(len(a))])
    for i in range(0, len(a)):
        if (ac[j]<1):
            if ac[j] == -1:
                omega[0,i] = w0[j]
            elif a[i] > ac[j]:
                omega[0,i] =  w0[j] + wa[j]*(1-a[i])
            elif(wa[j]>0):
                omega[0,i] =  -1.001
            elif(wa[j]<0):
                omega[0,i] =  -0.999
        if (ac[j]>1):
            omega[0,i] =  w0[j] + wa[j]*(1-a[i])
             
        omega_with_cross[0,i] = w0[j] + wa[j]*(1-a[i])
    omega_mat_with_cross = np.append(omega_mat_with_cross, omega_with_cross, axis = 0)
    omega_mat = np.append(omega_mat, omega, axis = 0)



fig = plt.figure(figsize = (16,5.5))
ax = fig.add_subplot(1,2,1)
for i in range(1,lines+1):
    ax.plot(a, omega_mat_with_cross[i],linestyle = "--", label = r"$\rm \omega$")
    ax.plot(a, omega_mat[i], label = r"$\rm \omega_{no_cross}$")

#ax.set_xlim(10**-3)

#ax.legend(fontsize = 13)
ax.set_xlabel("$a$", fontsize =20)
ax.set_ylabel(r"$\omega$", fontsize = 20)
ax.tick_params(axis='both', which='major', labelsize=15)