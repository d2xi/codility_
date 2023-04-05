def minPerimeterRectangle(area):
    """
    The function calculates the minmal perimeter of the rectangle having the given area.
    Args:
        area (int): An area of the rectangle represented by integer (>0).

    Returns:
        int: The minimal perimeter.
    """

    sideA = 1
    minPerim = 4 * area**2
    while sideA * sideA <= area:
        if area % sideA == 0:
            sideB = area//sideA
            perim = perimeterOfRectangle(sideA, sideB)
            minPerim = min(minPerim, perim)
        sideA += 1

    return minPerim


def perimeterOfRectangle(a, b):
    """
    The function for caluculates the perimeter of a rectangle with the given sides.
    Args:
        a (int): A side of the rectangle.
        b (int): A side of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    return 2*(a+b)
