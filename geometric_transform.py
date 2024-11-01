def apply_geometric_transform(img, p1, p2, transform):
    """
        Apply a geometric transform to a region with corners p1 and p2 of an image.
    """
    return img

def scale_region(img, p1, p2):
    """
        Scale region with corners p1 and p2 of an image.
    """
    transform = []
    return apply_geometric_transform(img, p1, p2, transform)

def rotate_region(img, p1, p2):
    """
        Rotate region with corners p1 and p2 of an image.
    """
    transform = []
    return apply_geometric_transform(img, p1, p2, transform)

def translate_region(img, p1, p2, x, y):
    """
        Translate region with corners p1 and p2 to q1 and q2 of an image.
    """
    transform = []
    return apply_geometric_transform(img, p1, p2, transform)


