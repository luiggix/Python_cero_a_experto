#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:05:05 2018

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt
#
# FuncAnimation: realiza una animación cambiando información apartir
# de la ejecución de una función de manera repetida (func)
#
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')
#
# Arreglos para generar datos para las gráficas
#
x = np.linspace(-3, 3, 61)
t = np.linspace(0, 25, 30)
#
# Creamos una malla para realizar las gráficas
#
xg, tg = np.meshgrid(x, t)
#
# Evaluamos una función complicada sobre la malla
#
A = np.sin(2 * np.pi * tg / tg.max())  # Amplitud
F = 0.95 * A * np.sinc(xg)  # Función: sin(x) / x
#
# ¿ Cuál es el tamaño y forma de la malla?
#
print(xg.shape, tg.shape, A.shape, F.shape, sep='\n')
#
# Preparamos la figura de tamaño (5,3) y los ejes donde
# se harán las gráficas
#
fig = plt.figure(figsize=(5,3))           # Figuras
ax = plt.axes(xlim=(-3, 3), ylim=(-1, 1)) # Ejes
#
# Se define el objeto "scat" graficando el primer conjunto de datos.
#
scat = ax.scatter(x[::3], F[0,::3])
#
# Función para cambiar los datos en la función para
# diferentes tiempos
#
def animate(i):
    # Must pass scat.set_offsets an N x 2 array
    y_i = F[i, ::3]
    scat.set_offsets(np.c_[x[::3], y_i])
#
# Usamos "FuncAnimation" para realizar la animación de los diferentes
# conjuntos de datos 
#
anim = FuncAnimation(fig,           # La figura
                     animate,       # la función que cambia los datos
                     interval=100,  # Intervalo entre cuadros en milisegundos
                     frames=30,     # Cuadros por segundo
                     repeat=True)   # Permite poner la animación en un ciclo


