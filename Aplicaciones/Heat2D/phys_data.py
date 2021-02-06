import matplotlib.image as mpimg

def readPhysData(filename):
    img=mpimg.imread(filename)
    k = img[:,:,0]
    Nx = k.shape[1]
    Ny = k.shape[0]
    for j in range(Nx):
        for i in range(Ny):
            if k[i,j] == 0.0:
                k[i,j] = 0.1
            if k[i,j] < 1.0:
                k[i,j] *= 0.01                

    return k.transpose()
