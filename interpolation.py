import numpy as np

def bilinear_interpolation(img):
    """
        Bilinear interpolation between pixels of an image.
    """

    # what we need to do:
    # 1. From image u (m * n), generate image v st 2m-3 * 2n-3 in both dimensions
    #   - Create new matrix
    #   - Copy the original pixels at the 2n-th position 
    # 2. For each row r in position m in image:
        # If m is even
            #  - For every pixel p (m,k) s.t k in range(n+1, 2n-3, 2)
                # - 
    # 3. Apply the function to the pixl

    return img

def _generate_bilinear_interpolation(points):
    if len(points) != 4:
        raise ValueError("Bilinear interpolation requires 4 points")
    
    A = np.array([[p.x, p.y, p.x * p.y, 1] for p in P])
    k = np.array([p.luminance for p in P])
    z = np.linalg.solve(A, k)

    a = z[0]
    b = z[1]
    c = z[2]
    d = z[3]

    return lambda x, y : a * x + b * y + c * x * y + d
