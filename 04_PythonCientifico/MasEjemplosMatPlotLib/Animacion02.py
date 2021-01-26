#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:35:18 2018

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')

#
# Generamos datos en 2D cambiantes con el tiempo
#
x = np.linspace(-3, 3, 91)
y = np.linspace(-3, 3, 91)
t = np.linspace(0, 25, 30)
xg, yg, tg = np.meshgrid(x, y, t)
A = np.sin(2 * np.pi * tg / tg.max())
F = A * (xg**2 + yg**2)
#F = A * np.sin(xg**2 + yg**2)
#F = A * np.sin(xg) * np.cos(yg)

#
# Figura y ejes
#
fig = plt.figure(figsize=(4,3))           # Figuras
ax = plt.axes(xlim=(-3, 3), ylim=(-3, 3)) # Ejes
#
# Se dibuja el primer conjunto de datos con mapa de color
#
cax = ax.pcolormesh(x, y, F[:-1, :-1, 0], vmin=-1, vmax=1, cmap='Oranges')
#
# Se dibuja la barra de colores
#
fig.colorbar(cax)
#
# Función para cambiar los datos dependientes del tiempo
#
def animate(i):
    cax.set_array(F[:-1, :-1, i].flatten()) # Set_array requiere un arreglo
#
# Usamos "FuncAnimation" para realizar la animación de los diferentes
# conjuntos de datos 
#
anim = FuncAnimation(fig,           # La figura
                     animate,       # la función que cambia los datos
                     interval=100,  # Intervalo entre cuadros en milisegundos
                     frames=30,     # Cuadros por segundo
                     repeat=True)   # Permite poner la animación en un ciclo



#plt.show()
