import sys
import matplotlib.image as mpimg
import numpy as np

def read(filename):
    try:
        in_file_name = sys.argv[1]
    except:
        mensaje = """ Error: La ejecucion de este programa es como sigue: 

            python heatConduction.py INPUT_01
        """
        print(mensaje)
        sys.exit(1)

    ifile = open(in_file_name, 'r') # abre el archivo de entrada
    ifile_lines = ifile.readlines() # lee las lineas del archivo
    ifile.close()                   # cierra el archivo de entrada

    a, b, c, d, A, B, C, D = ifile_lines[0].split() # separa las columnas de la primera linea

    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)

    A = float(A)
    B = float(B)
    C = float(C)
    D = float(D)

    # Lee la condicion inicial de una imagen
    img = mpimg.imread(filename)
    u = img[:,:,0]
    Nx = u.shape[1]
    Ny = u.shape[0]
    for i in range(Ny):
        for j in range(Nx):
            if u[i,j] == 0.0:
                u[i,j] = 0.1
            if u[i,j] < 1.0:
                u[i,j] *= 0.01          

    return (a,b,c,d,Nx-2,Ny-2,A,B,C,D,u)

