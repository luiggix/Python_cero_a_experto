#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:58:22 2018

@author: luiggi
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')
#
# Figura y ejes
#
#
# Figura y ejes
#
fig = plt.figure(figsize=(5,4))           # Figuras
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1)) # Ejes
ax.set_aspect('equal')

#
# Creamos la cadena a imprimir
#
mensaje = 'S.O.S Python es muy complicado'
label = ax.text(0, 0, mensaje[0],
                ha='center', va='center',
                fontsize=12)
#
# Función para cambiar los datos dependientes del tiempo
#
def animate(i):
    label.set_text(mensaje[:i+1])
    ax.set_ylabel('Time (s): ' + str(i/10))
    ax.set_xlabel('$x$')
    texto = '$\int_{%s}^{%s}$' % (i-1,i)
    ax.set_title('Integral = ' + texto + '$e^x dx$')
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
