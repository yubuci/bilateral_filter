import numpy as np

def gaussian_kernel(sigma_domain, radius = None): #if "radius = none" is not given, the funcition was a error 
    # because the if statement was not be executed and the variable "radius" was not be defined.
    
    if radius is None:
        radius = int(np.ceil(2 * sigma_domain))

    size = 2 * radius + 1
    c =np.zeros((size, size))

    for i in range(size):
        for j in range(size):

            x = i-radius
            y = j-radius
            c[i,j] = np.exp(-(x**2 + y**2)/(2*sigma_domain**2))


    return c 