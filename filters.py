import copy
import numpy as np

def spatial_filter(img, filter):
    """
        Apply a filter to an image.
    """

    m = len(img)
    n = len(img[0])
    u = len(filter)
    v = len(filter[0])
    new_img = copy.deepcopy(img)

    if u % 2 == 0 or v % 2 == 0:
        raise Exception("u and v must be odd for u*v filter")

    for i in range(u // 2, m - u // 2):
        for j in range(v // 2, n - v // 2):
            sum = 0
            for p in range(u):
                for q in range(v):
                    p_offset = i - u // 2 + p
                    q_offset = j - v // 2 + q
                    sum += filter[p][q] * img[p_offset][q_offset]
            
            new_img[i][j] = np.ceil(sum / (u * v))

    return new_img

def smoothing_filter(img, filter_size = 3):
    """
        Apply a smoothing filter to an image.
    """
    smoothing = np.ones((filter_size, filter_size))
    copy_matrix(img, spatial_filter(img, smoothing))

def sharpening_filter(img):
    """
        Apply a sharpening filter to an image.
    """
    m = len(img)
    n = len(img[0])
    sharpening = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    laplacian = spatial_filter(img, sharpening)

    for i in range(m):
        for j in range(n):
            img[i][j] -= laplacian[i][j]

def edge_detection_filter(img):
    """
        Apply an edge detection filter to an image.
    """
    edge_detection = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    copy_matrix(img, spatial_filter(img, edge_detection))

def copy_matrix(target, source):
    m = len(source)
    n = len(source[0])
    for i in range(m):
        for j in range(n):
            target[i][j] = source[i][j]