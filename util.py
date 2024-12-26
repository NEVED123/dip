def copy_matrix(target, source):
    m = len(source)
    n = len(source[0])
    for i in range(m):
        for j in range(n):
            target[i][j] = source[i][j]

def matrix_dimensions(matrix):
    """
    Returns (m,n). 
    """
    return len(matrix), len(matrix[0])