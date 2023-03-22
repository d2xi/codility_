def countAbsDistinctValues(A):
    """
    Calcluates the number of absolute distict values present in the given list of integers.
    
    Examples:

    - [5]     -> 1
    - [5,5]   -> 1
    - [-5,5]  -> 1
    - [1,2,3] -> 3
 
    Args:
        A (list of int): The list of integers sorted in assedning order.

    Returns:
        int: The count of unique abolute values present in the given integer list.
    """
    beg=0
    end=len(A)-1
    absDistinctCounter = 0
    prevAbsValue = None
    currAbsValue = None
    while beg <= end:

        tail = abs(A[beg])
        head = abs(A[end])
        prevAbsValue = currAbsValue
        if tail <= head:
            currAbsValue = head
            end -= 1
        else:
            currAbsValue = tail
            beg+=1

        if currAbsValue != prevAbsValue:
            absDistinctCounter+=1

    return absDistinctCounter