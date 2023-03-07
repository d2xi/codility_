def getMinNumberNails(plkHeads, plkTails, nailingOrder):
    """
    The functions calculates the minimal number of nails required to mount all planks,
    considering the provided nailing order (nailingOrder).

    For each plank with id "i" (plkHeads[i], plkTails[i]) the condition must be fulfiled:
    plkHeads[i] < plkTails[i].

    Args:
        plkHeads (list): The list of integers(>=0) representing left most position of the planks .
        plkTails (list): The list of integers(>=0) represeinting right most position of the planks.
        nailingOrder (list): The list of integers(>=0) representing an nailing order to follow(unsorted). Each integer represents a naling position.

    Returns:
        int: The minimal number of nails required.
    """
    nailingOrderSortedByPostions= sorted(enumerate(nailingOrder),key=lambda entry:entry[1])
    plank2nail= []
    for (begPos,endPos) in zip(plkHeads, plkTails):
        idTupleBeg = getIdLeftMostNalingPosition(begPos,endPos,nailingOrderSortedByPostions)
        if(idTupleBeg == -1):
            return -1
        idTupleBest = getEarliestNalingPosition(idTupleBeg,endPos,nailingOrderSortedByPostions)
        (idBestPos,_) = nailingOrderSortedByPostions[idTupleBest]
        plank2nail.append(idBestPos)
    minNumerNails = max(plank2nail) + 1
    #minNumerNails = len(set(plank2nail))
    return minNumerNails

def getIdLeftMostNalingPosition(plkBegPos, plkEndPos, nalingOrder):
    """
    The function returns an index of the left most posible naling position for the given plank (plkBegPos,plkEndPos).
    
    Args:
        plkBegPos (int): The plank start position.
        plkEndPos (int): The plank end position.
        nailingOrder (list): The list of tuples (idPosition, nailingPosition) sorted by positions in ascending order.
        
    Returns:
        int: The index in `nailingOrder` of the tupel corresponding to the left most nailing position.
    """
    beg = 0
    end = len(nalingOrder)-1
    idTuple = -1
    leftMostPos = -1
    while(beg<=end):
        mid = (beg+end)//2
        (_,pos) = nalingOrder[mid]
        if(pos<plkBegPos):
            beg = mid + 1
        elif(pos>plkEndPos):
            end = mid - 1
        else:
            end = mid - 1
            if(pos<leftMostPos or idTuple<0):
                idTuple = mid
                leftMostPos = pos
    return idTuple


def getEarliestNalingPosition(begPos, plkEnd, nalingOrder):
    """
    The function returns an id of a tuple — (idPos, pos) — from `nailingOrder` such that certain conditions are met:
    1. tuple id > `begPos`
    2. pos <= `plkEnd`
    3. `idPos` is minimal
    
    does a linear search on `nalingOrder` starting with `begPos` until the condition  tupel[2] <= `plkEnd` is met.

    Args:
        begPos (int): The search starting position.
        plkEndPos (int): The plank end position.
        nailingOrder (list): The list of tuples (idPosition, nailingPosition) sorted by positions in ascending order.

    Returns:
        int: The index in `nailingOrder` of the tupel — (idPos, pos) — with minimal `idPos`
    """
    idTuple = begPos
    idTupleBest = -1
    minIdPos = -1
    pos = -1
    while(idTuple < len(nalingOrder)):
        (idPos,pos) = nalingOrder[idTuple]
        if(pos>plkEnd):
            break
        if (minIdPos>idPos or minIdPos<0):
            minIdPos = idPos
            idTupleBest = idTuple
        idTuple = idTuple + 1

    return idTupleBest