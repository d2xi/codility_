def countTriangles(nums):
    """
    Calculates the number of triangles that can be constracted by using positions from the provided list.

    Args:
        nums (int list): List of integers >0, that may be empty.

    Returns:
        int: Number of triagles.
    """
    beg = 0
    end = len(nums)-1
    sortedNums = sorted(nums)
    numTriangles = 0
    for posB in range(beg+1, end):
        posA, posC = beg, posB+1
        valB = sortedNums[posB]
        while posA < posB and posC <= end:
            valA, valC = sortedNums[posA], sortedNums[posC]
            if valC-valA < valB:
                numTriangles += posB-posA
                posC += 1
            else:
                posA += 1
    return numTriangles
