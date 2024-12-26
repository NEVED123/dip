import numpy as np
import util

def add_random_noise(img, stddev):
    m, n  = util.matrix_dimensions(img)
    for i in range(m):
        for j in range(n):
            l = np.random.normal(loc=img[i][j], scale=stddev)
            if l > 255:
                l = 255
            if l < 0:
                l = 0

            img[i][j] = l

def reduce_gaussian_noise(imgs):
    """
    Uses a set of noisy images to find the ground truth image.
    """
    m, n = util.matrix_dimensions(imgs[0])
    k = len(imgs)
    for i in range(1, k):
        if util.matrix_dimensions(imgs[i]) != (m,n):
            raise Exception("Not all images are the same size.")
        
    truth_img = np.zeros((m, n))

    for img in imgs:
        for i in range(m):
            for j in range(n):
                truth_img[i][j] += img[i][j] // k
    
    return truth_img