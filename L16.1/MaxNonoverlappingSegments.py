def maxNumberNonoverlappingSegments(segBegs, segEnds):
    """
    Returns the maximum number of non-overlapping segments for a given list of segments sorted by their end positions. Each segment is represented by its beginning and end position. 
 
    Args:
        segBegs (int list): A list of segments starts
        segEnds (int list): A list of segments ends sorted in ascending order.

    Returns:
        int: The maximal number of non-overlapping segments
    """
    numSegs = len(segBegs)
    numNonoverlappingSegments = 0
    prevSegEnd = -1
    for currSegId in range(0, numSegs):
        if segBegs[currSegId] > prevSegEnd:
            numNonoverlappingSegments += 1
            prevSegEnd = segEnds[currSegId]
            currSegId += 1
    return numNonoverlappingSegments
