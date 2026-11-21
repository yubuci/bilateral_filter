from skimage import data
from skimage.color import rgb2gray
import numpy as np

def load_gray(name): # load a image from skimage.data and convert it to grayscale if it is RGB

    x = getattr(data,name)
    image = x()

    if (image.ndim == 3):
        image = rgb2gray(image)*255
    else:
        image = image.astype(np.float64)
    
    return image

def load_rgb(name):

    y = getattr(data,name)
    image = y()

    image = image.astype(np.float64)
    return image

def make_step(r,c,low,high, noise_sigma, seed):

    image = np.full((r,c),low, dtype=np.float64)
    image[:,c//2:] = high

    rng  = np.random.default_rng(seed)
    noise = rng.normal(0, noise_sigma, (r,c))
    image = image + noise

    return image
    


    






