def getNumberChocolatesEaten(totalNumChocolates, skipCount):
    eatenCount = 0
    wrappers = []
    currPos = 0
    while(True):
        if (currPos not in wrappers):
            eatenCount = eatenCount + 1
            wrappers.append(currPos)
        else:
            return eatenCount
        currPos = (currPos + skipCount) % totalNumChocolates