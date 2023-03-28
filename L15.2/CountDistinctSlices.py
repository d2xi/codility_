def countDistinctSlices(nums):
    """
    Calculates the number of slices having no duplicate values. A valid slice is a pair of indexes: start and end, such that start <= end.
    An examples of valid slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4).

    Args:
        nums (int list): Non empty list of integers(>=0).

    Returns:
        int: Number of slices with no duplicate. Returns 1E9, if the resulting number is greater than 1E9.  
    """
    beg = 0
    end = len(nums)-1
    if len(nums) == 0:
        return 0
    posTail = beg
    posHead = beg
    latestEncounters = {}
    numSlices = 0
    increment = 1
    while posHead <= end:
        valueHead = nums[posHead]
        posLastEncounter = latestEncounters.get(valueHead, -1)
        if posLastEncounter >= posTail:
            posTail = posLastEncounter + 1
            increment = posHead - posTail + 1
        else:
            numSlices += increment
            latestEncounters[valueHead] = posHead
            posHead += 1
            increment += 1
        if numSlices > 1E9:
            return int(1E9)
    return numSlices
