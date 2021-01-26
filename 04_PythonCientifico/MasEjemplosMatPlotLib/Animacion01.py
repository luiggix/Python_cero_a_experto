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
# Dibujamos todas las figuras en una sola gráfica. Esto lo hacemos 
# solo para verificar que la función está bien calculada.
#
#for i in range(0,30):
#    line = ax.plot(x, F[i, :], color='b', lw=2)[0]
#
# Se define el objeto "line" graficando el primer conjunto de datos.
#
line = ax.plot(x, F[0, :], color='b', lw=2)[0]
print(type(line))
#
# Función para cambiar los datos en la función para
# diferentes tiempos
#
def animate(i):
    line.set_ydata(F[i, :]) # cambia los datos en la dirección y
#
# Usamos "FuncAnimation" para realizar la animación de los diferentes
# conjuntos de datos 
#
anim = FuncAnimation(fig,           # La figura
                     animate,       # la función que cambia los datos
                     interval=100,  # Intervalo entre cuadros en milisegundos
                     frames=30,     # Cuadros por segundo
                     repeat=True)   # Permite poner la animación en un ciclo

plt.show()

#anim.save('animacion.mp4', fps=10)
