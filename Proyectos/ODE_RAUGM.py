#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:41:50 2019

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt

def Euler(x, dt, f):
    return x + dt * f(x)

def RK2(x, dt, f):
    return x + dt * f(x + 0.5 * dt * f(x))

def RK4(x, dt, f):
    k1 = dt * f(x)
    k2 = dt * f(x + 0.5 * k1)
    k3 = dt * f(x + 0.5 * k2)
    k4 = dt * f(x + k3)
    return x + (k1 + 2*k2 + 2*k3 + k4) / 6
    
def lorenz_deriv(x_y_z, sigma=10.0, beta=8./3, rho=28.0):
    '''
    Cálculo de las ecuaciones de Lorenz
    '''
    x, y, z = x_y_z
    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])

if __name__ == '__main__':
    
    N = 10 # Número de trayectorias en el espacio fase
    Nt = 100 # Número total de pasos
    dt = 0.01 # Stepsize
    
    #Posiciones iniciales
    np.random.seed(1)
    x0 = -15 + 30 * np.random.random((N, 3))
    
    # Figura
    fig = plt.figure();
    ax = fig.add_axes([0, 0, 1, 1], projection='3d');
    ax.plot(x0[:,0], x0[:,1], x0[:,2], '.') # condicion inicial
    
    # Solución de las ecs. de Lorenz usando el método de Euler
    for t in range(Nt):
        x0 = np.asarray([Euler(x, dt, lorenz_deriv) for x in x0])
    #    x0 = np.asarray([RK2(x, dt, lorenz_deriv) for x in x0])
    #    x0 = np.asarray([RK4(x, dt, lorenz_deriv) for x in x0])
    
        ax.plot(x0[:,0], x0[:,1], x0[:,2], '.')
    
    plt.show()
