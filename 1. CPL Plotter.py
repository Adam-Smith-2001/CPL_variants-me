#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:57:48 2024

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
#%%
#Background
data = np.loadtxt("Documents/GitHub/CPL/output/CPL00_background.dat")
data = data[22000:, :]
#data = np.loadtxt("Useful_outputs/Weak_Coupling,10-5/Weak_Coupling00_background.dat")

factor = (3.81*10**56)**2
rho_tot = data[:, 15]*3

z = data[:,0]
rho_cdm1 = data[:,10]*3/factor
rho_scf = data[:,11]*3/factor
rho_b = data[:,9]*3/factor
rho_phot = data[:,8]*3/factor
#rho_ax = data[:, 30]*3/factor
#v_phi = data[:, 20]/factor
#v_ax = data[:, 29]

testplot = (rho_b+rho_cdm1)/(1+z)**3

z = data[:, 0]
a=1/(1+z)

fig = plt.figure(figsize = (16,5.5))
ax = fig.add_subplot(1,2,1)
#plt.tick_params(axis = "x",which = "major", bottom = False,labelbottom=False)

ax.set_yscale('log')
ax.set_xscale("log")

#ax.plot(a, testplot, label="testplot")
ax.plot(a, rho_scf,color = "C1", label = r"$\rm \Lambda$")
ax.plot(a, rho_cdm1,color = "C0", label=r"$\rm CDM$")
#ax.plot(a, v_phi,color = "C5",label=r"$\rm Dilaton\; potential$")
ax.plot(a, rho_b,color = "C2", label=r"$\rm Baryons$")
ax.plot(a, rho_phot,color = "C3", label=r"$\rm Radiation$")

ax.legend(fontsize = 13)
ax.set_xlabel("$a$", fontsize =20)
ax.set_ylabel(r"$\rho(M_{P}^4)$", fontsize = 20)
ax.tick_params(axis='both', which='major', labelsize=15)

yticks = [10**-120, 10**-115, 10**-110, 10.**-105, 10.**-100]
yticklabels = [r"$10^{-120}$", r"$10^{-115}$", r"$10^{-110}$", r"$10^{-105}$", r"$10^{-100}$"]
ax.set_yticks(yticks, labels = yticklabels)

xticks = [10**-6, 10**-5, 10**-4, 10.**-3, 10.**-2, 10.**-1, 10.**0]
xticklabels = [r"$10^{-6}$", r"$10^{-5}$", r"$10^{-4}$", r"$10^{-3}$", r"$10^{-2}$", r"$10^{-1}$", r"$10^{0}$"]
ax.set_xticks(xticks, labels = xticklabels)

plt.ylim(10**-125)

ax.grid()
#Omegas
data = data[:,:]
rho_crit = data[:, 15]*3

z = data[:,0]
omega_cdm1 = data[:,10]*3/rho_crit
omega_scf = data[:,11]*3/rho_crit
omega_b = data[:,9]*3/rho_crit
omega_rad = (data[:,8]+data[:, 14])*3/rho_crit

#v_phi = data[:, 18]

z = data[:, 0]
a=1/(1+z)

ax1 = fig.add_subplot(1,2,2)

#ax.set_yscale('log')
ax1.set_xscale("log")


ax1.plot(a, omega_scf,color = "C1", label = r"$\rm \Lambda$")
ax1.plot(a, omega_cdm1,color = "C0", label=r"$\rm CDM$")
ax1.plot(a, omega_b,color = "C2", label=r"$\rm Baryons$")
ax1.plot(a, omega_rad,color = "C3", label=r"$\rm Radiation$")
#ax1.plot(a, omega_ax, label=r"$\rm Axion$")

yticks = [0, 0.2,0.4, 0.6, 0.8, 1]
yticklabels = [r"$0$", r"$0.2$", r"$0.4$", r"$0.6$", r"$0.8$", r"$\rm 1$"]
ax1.set_yticks(yticks, labels = yticklabels)

xticks = [10**-4, 10**-3, 10**-2, 10.**-1, 10.**0]
xticklabels = [r"$10^{-4}$", r"$10^{-3}$", r"$10^{-2}$", r"$10^{-1}$", r"$10^{0}$"]
ax1.set_xticks(xticks, labels = xticklabels)

plt.xlim(7*10**-6, 1.3)

ax1.legend(fontsize = 13, loc ="upper left")
ax1.grid()
ax1.set_xlabel("$a$", fontsize =20)
ax1.set_ylabel(r"$\Omega$", fontsize = 20)
ax1.tick_params(axis='both', which='major', labelsize=15)
fig.show()
#plt.savefig("background", dpi = 300,  bbox_inches="tight")
#%%
#Equation of state
data = np.loadtxt("Documents/GitHub/CPL/output/CPL09_background.dat")
data = data[22000:, :]


z = data[:,0]
a=1/(1+z)
rho_scf = data[:,11]*3
p_scf = data[:,20]*3
omega = p_scf/rho_scf

fig = plt.figure(figsize = (16,5.5))
ax = fig.add_subplot(1,2,1)
#plt.tick_params(axis = "x",which = "major", bottom = False,labelbottom=False)

#ax.set_xscale("log")

#ax.plot(a, testplot, label="testplot")
ax.plot(a, omega,color = "C1", label = r"$\rm \Lambda$")
ax.set_xlim(10**-3)
ax.set_ylim(-3, 2)
#ax.legend(fontsize = 13)
ax.set_xlabel("$a$", fontsize =20)
ax.set_ylabel(r"$\omega$", fontsize = 20)
ax.tick_params(axis='both', which='major', labelsize=15)
#%%Theoretical EoS
#Equation of state
z = data[:,0]
a = 1/(1+z)
w0 = -1.6
wa = -1.5
omega =w0 + wa*(1-a)

fig = plt.figure(figsize = (16,5.5))
ax = fig.add_subplot(1,2,1)
#plt.tick_params(axis = "x",which = "major", bottom = False,labelbottom=False)

ax.set_xscale("log")

#ax.plot(a, testplot, label="testplot")
ax.plot(a, omega,color = "C1", label = r"$\rm \Lambda$")
ax.set_xlim(10**-3)

#ax.legend(fontsize = 13)
ax.set_xlabel("$a$", fontsize =20)
ax.set_ylabel(r"$\omega$", fontsize = 20)
ax.tick_params(axis='both', which='major', labelsize=15)
#%% Power Spectra
#data = np.loadtxt("output/LCDM01_pk.dat")
data1 = np.loadtxt("Documents/GitHub/CPL/output/CPL00_pk.dat")
data = np.loadtxt("Desktop/Paper_Plots/LCDM/lcdm00_pk.dat")
#data1 = np.loadtxt("Useful_outputs/Weak_Coupling,10-5/Weak_Coupling00_pk.dat")


fig = plt.figure(figsize = (9, 6.5))
ax = fig.add_subplot(1,1,1)
ax.plot(data[:,0], data[:,1], label = "Normal LCDM")
ax.plot(data1[:,0], data1[:,1], "--",label = r"Yoga $g = -0.2, g_a = -5\times 10^{-28}, \zeta = yoga val$")

ax.set_ylabel("$P_k (Mpc/h)^3$")
ax.set_xlabel("$k (h/Mpc)$")

ax.set_yscale('log')
ax.set_xscale('log')

ax.legend()
#%%
data1 = np.loadtxt("Documents/GitHub/CPL/output/CPL00_cl.dat")
data = np.loadtxt("Desktop/Paper_Plots/LCDM/lcdm00_cl.dat")

fig = plt.figure(figsize = (9, 6.5))
ax = fig.add_subplot(1,1,1)
#ax.plot(data[:,0], data[:,1], label = "Normal LCDM")

ax.plot(data[:,0], data[:,1],label = "LCDM")
ax.plot(data1[:,0], data1[:,1],label = r"Yoga $g_{(B)} = -0.4, g_{(CDM)} = -g_{(B)}/5,g_a = -5\times 10^{-28}, \zeta = yoga val$")
#ax.plot(data2[:,0], data2[:,1],"--",label = r"Yoga $g_{(B)} = -0.4, g_{(CDM)} = -g_{(B)}/5,g_a = -5\times 10^{-28}, \zeta = yoga val$")

#ax.plot(data2[:,0], data2[:,1], "--",label = "YOGA orig")

ax.set_ylabel(r"$l(l+1)C_l^{TT}/2\pi$")
ax.set_xlabel("$l $")

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([5*10**0, 2*10**3])
ax.set_ylim([2.5*10**-11, 9*10**-10])
#ax.legend()







