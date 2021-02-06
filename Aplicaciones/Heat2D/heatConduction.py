import read_data as rd
import meshes as ms
import phys_data as pd 
import finite_differences as fd 
import solvers as sol
import numpy as np
#
# Lee los datos de la simulación numérica
#
(a,b,c,d,Nx,Ny,bA,bB,bC,bD,u) = rd.read('Mexico50_R90.png')
print('a = {}, b = {}, c = {}, d = {}'.format(a,b,c,d))
print('bA = {}, bB = {}, bC = {}, bD = {}'.format(bA,bB,bC,bD))
print('Nx = {}, Ny = {}'.format(Nx,Ny))
#
#
# Crea la malla del dominio
#
Lx, Ly, hx, hy, x, y = ms.createMesh(a,b,c,d,Nx,Ny)
#
# Grafica la condición inicial
#
colormap ='inferno'
#
# Conductividad térmica
#
k = np.ones((Ny+2,Nx+2))
#k = pd.readPhysData('TUX50.png')
#
# Prepara el sistema de ecuaciones a resolver
#
ht = 0.001
Tmax = 0.02
Nmax = int(Tmax/ht)
r = ht /(hx * hy)
f = fd.initRHS(Nx,Ny)
fd.dirichlet(f,u,bA,bB,bC,bD)
A = fd.laplacian2D(Nx,Ny,r,k,1)
#
# Fuente
#
source = 0.0
#
# Inicia el cálculo de la solución dependiente del tiempo
#
anim_3D = input('Para animación en 3D teclea <3> y luego <enter> : ')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')
#
# Malla
#
xg, yg = np.meshgrid(x,y)
#
# Figura y ejes
#
if anim_3D:
    fig = plt.figure(figsize=(5,4))           # Figuras
    ax = Axes3D(fig)
#
# Se dibuja el primer conjunto de datos usando superfice
#
    cax = ax.plot_surface(xg, yg, u.T, alpha=.95, cmap=colormap)
else:
    fig = plt.figure(figsize=(5,4)) 
    ax = plt.axes(xlim=(0, 1), ylim=(0, 1)) # Ejes
#
# Se dibuja el primer conjunto de datos usando contornos
#
    cax = ax.contourf(xg, yg, u, alpha=.95, cmap=colormap)


def animate(i):
#
# Resuelve el sistema lineal
#
    print('Paso {}'.format(i))
    f = np.copy(u[1:Ny+1,1:Nx+1])
#	f[si,sj] = source
    sol.solve(A,u,f)
    fd.dirichlet(f,u,bA,bB,bC,bD)
#
# Visualiza la solución
#
    ax.collections = []
    if anim_3D:
        ax.plot_surface(xg, yg, u.T, alpha=.95, cmap=colormap)
    else:
        ax.contourf(xg, yg, u.T, 100, alpha=.95, cmap=colormap)

#
# Función que controla la animación
#
anim = FuncAnimation(fig,           # La figura
                     animate,       # la función que cambia los datos
                     interval=100,  # Intervalo entre cuadros en milisegundos
                     frames=Nmax,     # Cuadros por segundo
                     repeat=False)   # Permite poner la animación en un ciclo

plt.show()

