import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def surface(x,y,u,i,colormap,name = 'False'):
    xg, yg = np.meshgrid(x,y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xg, yg, u.T, rstride=2, cstride=2, alpha=.95, cmap=colormap)
    if name != 'False':
        plt.savefig(name)
    titulo = 'Paso : {}'.format(i)
    plt.title(titulo)
    plt.show()

def contour(x,y,u,i,colormap,name = 'False'):
    xg, yg = np.meshgrid(x,y)
    plt.contourf(xg, yg, u.T, 100, alpha=.95, cmap=colormap)

    if name != 'False':
        plt.savefig(name)

    titulo = 'Paso : {}'.format(i)
    plt.title(titulo)
    plt.show()

def write(x,y,u,out_file_name):
	ofile = open(out_file_name,'w') # abre archivo para salida
	for i in range(0,x.size):
		for j in range(0,y.size):
			ofile.write('%12.10g \t %12.10g \t %12.10g\n' % (x[i], y[j],u[j,i]))
	ofile.close()
