def countTriangles(nums):
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
                print(valA, valB, valC)
            else:
                posA += 1
    return numTriangles
