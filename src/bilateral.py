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

def bilateral_gray_naive(image, sigma_domain, sigma_range, radius = None):
    if radius is None:
        radius = int(np.ceil(2 * sigma_domain))

    c = gaussian_kernel(sigma_domain, radius)

    border_reflect = np.pad(image,radius, mode ="reflect")
    #not zero padding because it will create a black border around the image and it will affect the result of the filter.

    x, y = image.shape
    output = np.zeros_like(image) #empty matrix with the same shape as the input image

    for i in range(x):
        for j in range(y):
            window = border_reflect[i : i + 2 * radius + 1, j : j + 2 * radius + 1]
            center = image[i, j]
            s = np.exp(-((window - center)**2)/(2*sigma_range**2))
            bilateral_w = c*s

            output[i,j]= np.sum(bilateral_w *window)/np.sum(bilateral_w) #output with normalization
    
    return output