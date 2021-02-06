#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:10:45 2020

@author: luiggi
"""
import matplotlib.pyplot as plt
from math import ceil

def maxminTicks(paises):
    """
    Calcula el máximo y el mínimo de todos los países y los yticks.
    
    Parameters
    ----------
    paises : DataFrameGroupBy
        Dataframe generado por GroupBy con la información de los países.
        
    Returns
    -------
    p_max, y_max, yticks, p_min, y_min 
        El país con el máximo valor, el valor máximo, la lista para los yticks,
        el país con el valor mínimo y el valor mínimo.
    """
    y_max = 0
    y_min = 10
    for p in paises.groups.keys():
        temporal = paises.get_group(p)['Value'].max()
        if y_max < temporal:
            y_max = temporal
            p_max = p
            
        temporal = paises.get_group(p)['Value'].min()
        if y_min > temporal:
            y_min = temporal
            p_min = p        
        
    yticks = [i for i in range(0,ceil(y_max)+1)]
    return p_max, y_max, yticks, p_min, y_min

def inicializaGrafica(y_maximo, yticks):
    """
    Inicializa algunos parámetros de la figura (el canvas).
    
    Parameters
    ----------
    y_maximo : int
        Valor máximo para el eje y.
    
    yticks : list
        Lista de valores para los ticks en el eje y.
    """
    fig = plt.figure(figsize=(12,6)) # Cambiamos el tamaño de la figura
    plt.xticks(rotation=70, fontsize=8)
    plt.xlim(14,-2,-1)
    plt.ylim(0,y_maximo)   # Límites en el eje y (usamos y_maximo)
    plt.yticks(yticks)     # Marcas en el eje y
    plt.grid(ls='--', lw=0.5, c='#AAAAAA') # Rejilla en color adecuado para fondo negro.

    # Información adicional y títulos
    plt.title('Promedio de número de hijos por mujer', loc='left', fontsize=12)
    plt.title('fuente: http://data.un.org', loc='right', fontstyle='italic', fontsize=10, c='blue')
    plt.suptitle(' Comparación de la fertilidad', y = 0.975, fontsize=14)

    ejes = plt.gca() # Obtenemos los ejes y eliminamos las spines
    ejes.spines['right'].set_visible(False)
    ejes.spines['top'].set_visible(False)
    ejes.spines['left'].set_visible(False)
    ejes.spines['bottom'].set_visible(False)
    
    # Modificamos algunos parámetros de los ticks en el eje y
    ejes.tick_params(axis='y', width=1, length=25)
    
    # Realizamos algunas anotaciones sobre el gráfico base
    plt.annotate('Nivel de \n reemplazo: \n promedio = 2.1', xy=(12.5, 2.12), xytext=(12.5, 0.5),
                 bbox=dict(boxstyle='round', facecolor='green', edgecolor='black', alpha=0.5, linewidth=0.75),
                 arrowprops=dict(arrowstyle='->', facecolor='black', edgecolor='black'),
                 fontsize=10, color='black', horizontalalignment='center')

    plt.text(0.5, 7.75, 'Cada línea representa la \n evolución del promedio  \n de hijos por mujer en un país',                   
             transform=plt.gca().transData, 
             horizontalalignment='center', color='black',
             bbox=dict(boxstyle='round', facecolor='green', edgecolor='black', alpha=0.5, linewidth=0.75))  
    
    return fig, ejes
        
def graficaFertilidad(paises, parametros={}):
    """
    Realiza la gráfica de todos los países.
    
    Parameters
    ----------
    paises : DataFrameGroupBy
        Dataframe generado por GroupBy con la información de los países.
    
    parametros : dict
        Parámetros para generar la gráfica.
    """
    for p in paises.groups.keys():
        pais = paises.get_group(p)
        plt.plot(pais['Year(s)'], pais['Value'], zorder=1, **parametros) 
        
    # Al final de todas las gráficas ponemos la del nivel de reemplazo 
    plt.plot([14,-1],[2.1,2.1], 'k--', lw=1.0, zorder=5)
        
def graficaFertilidadUnPais(paises, p, limit=0, parametros={}, par_glow = None, zorder=2):
    """
    Realiza la gráfica de un solo país con realce para fondo negro.
    
    Parameters
    ----------
    paises : DataFrameGroupBy
        Dataframe generado por GroupBy con la información de los países.
    
    parametros : dict
        Parámetros para generar la gráfica.
    
    par_glow : dict
        Diccionario con los parámetros para resaltar las curvas con un "halo" 
        a su alrededor. Cuando par_glow = None (defalt) no se hace nada. En otro
        caso es conveniente pasar la transparencia y el color. Esta
        curva se dibuja por detrás de la curva principal, con un ancho mayor y el
        color definido
        Ejemplo:
                par_glow = {'alpha':0.4, 'c':'yellow'}
    """
    pais = paises.get_group(p)

    line_glow = [False]
    
    if par_glow:
    # Se grafica una curva con una línea 3 veces más ancha que la original
    # y transparente para resaltarla. 
        line_glow = plt.plot(pais['Year(s)'][limit:14], 
                             pais['Value'][limit:14], lw=parametros['lw']*3, zorder=zorder, **par_glow)

    # Se grafica la curva del país con los parámetros necesarios.
    line = plt.plot(pais['Year(s)'][limit:14], 
                    pais['Value'][limit:14], zorder=zorder, **parametros)

    # Ponemos un texto al final de la curva para mostrar el 
    # nombre del país y el valor final de fertilidad
    pais_val = pais['Value'].iloc[limit]
    text = plt.text(x = limit, y = pais_val, 
                    s = ' {} {:1.2f}'.format(p, pais_val), 
                    c = line[0].get_color(), weight = 'bold')
    
    # Ponemos el valor inicial de fertilidad al principio de la curva.
    pais_val = pais['Value'].iloc[13] 
    plt.text(x = 13.75, y = pais_val, 
             s = '{:1.2f} '.format(pais_val), 
             c = line[0].get_color(), weight = 'bold')

    return line[0], line_glow[0], text
