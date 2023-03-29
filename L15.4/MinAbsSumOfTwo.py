def minAbsSumOfTwo(nums):
    """
    Returns the minimal absolute value of a sum of two elements possible for the given list of values. 
    Args:
        nums (int list): Non-empty list of integers.

    Returns:
        int: The minimal absolute value of a sum of two elements among all possibilities.
    """
    sortedNums = sorted(nums)
    beg = 0
    end = len(sortedNums)-1
    posTail = beg
    posHead = end
    minAbsSum = 2*abs(sortedNums[end])
    while posTail <= posHead:
        sum = sortedNums[posTail] + sortedNums[posHead]
        minAbsSum = min(minAbsSum, abs(sum))
        if sum == 0:
            break
        if sum > 0:
            posHead -= 1
        else:
            posTail += 1
    return minAbsSum
