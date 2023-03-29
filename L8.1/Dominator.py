def getIndexOfDominator(nums):
    """
    The function returns any of the indices of the dominator value (the value, that occurs more than half the time) in the given list.
    Args:
        nums (int list): List of integer values.

    Returns:
        int: Index of dominator.
    """
    indexStack = []
    moreThanHalve = len(nums)//2+1
    dominatorIndex = -1
    stackSize = 0
    stackTopVal = None
    for idVal, currVal in enumerate(nums):
        if stackSize > 0 and currVal != stackTopVal:
            indexStack.pop()
        else:
            indexStack.append(idVal)
            stackTopVal = currVal
        stackSize = len(indexStack)

    if stackSize > 0 and countOccurence(stackTopVal, nums) >= moreThanHalve:
        dominatorIndex = indexStack.pop()

    return dominatorIndex


def countOccurence(val, nums):
    """
    The function counts the occurrence of the given number in the list.    
    Args:
        val (int): The value for which the occurrence is to be counted.
        nums (int list): A list of integers.

    Returns:
        int: The occurrence count of the number in the list.
    """
    occurencyCount = 0
    for currNum in nums:
        if currNum == val:
            occurencyCount += 1
    return occurencyCount
