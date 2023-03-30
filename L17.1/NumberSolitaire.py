def numberSolitaire(nums):
    """
    The function calculates the maximal sum that can be obtained out of given list of numbers. First and the last numbers are always included, also even though some numbers may be skipped,
    although the distance between the lasted picked number and next picked number is never more than six. 
    Args:
        nums (int list): A list of integers(>=-1E4) with at least two values.
    """
    lowerBoundary = -1E4-1
    numElements = len(nums)
    maxDiceVal = 6
    maxSumForLastSixPos = [lowerBoundary]*maxDiceVal
    maxSum = 0
    for pos in range(0, numElements):
        currVal = nums[pos]
        maxSumForLastSixPos.append(currVal + maxSum)
        maxSumForLastSixPos.pop(0)
        maxSum = max(maxSumForLastSixPos)
    maxSum = maxSumForLastSixPos.pop()        
    return maxSum
