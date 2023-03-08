def getNumberChocolatesEaten(totalNumChocolates, stepsToNextPos):
    """
    The function calculates the number of chocolates to be eaten until a wrapper is met. Chocolates are aranged in a circle.
    When a chocolate is eaten it replaced with a wrapper.

    Args:
        totalNumChocolates (int): An integer from the interval [1..1,000,000,000], which represents total number chocolates given.
        stepsToNextPos (int): An integer from the interval [1..1,000,000,000]. currentPosition + stepsToNextPos = nextPosition

    Returns:
        int: The number of eaten chocolates.
    """
    return totalNumChocolates // gcd(stepsToNextPos,totalNumChocolates)

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)