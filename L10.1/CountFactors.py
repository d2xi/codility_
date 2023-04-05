def countFactors(num):
    """
    The function calculatest the number of factors of the given number.
    Args:
        num (int): An integer (>0).

    Returns:
        num (int): The number of factors.
    """
    fac = 1
    facCount = 0
    while fac * fac < num:
        divRest = num % fac
        if divRest == 0:
            facCount += 2
        fac+=1
    if fac*fac == num:
        facCount += 1
    return facCount