def countPairsWithAllPrimeDivisorsCommon(A, B):
    """
    The function calculation the number of integer pairs (A[i],B[i]) having the exact the same set of prime factors.

    Args:
        A (int[]): Array of integers
        B (int[]): Array of integers

    Returns:
        int: The pair count having exact the same set of prime factors. 
    """
    counter = 0
    for (a,b) in zip(A,B):
        if(haveAllPrimeDivisorCommon(a,b)==1 and haveAllPrimeDivisorCommon(b,a)==1):
            counter += 1
    return counter

def haveAllPrimeDivisorCommon(a, b):
    """
    The funciton returns 1 if given pair of numbers (a,b) have the same set of prime factors.

    Args:
        a (int): Integer
        b (int): Integer

    Returns:
        int: 1, if a and b have same set of prime factors, 0 otherwise
    """
    g = gcd(a,b)
    if(a==1 and b==1):
        return 1
    elif(g == 1):
        return 0
    else:
        k = a//g
    if(k==1):
        return 1
    else:
        return haveAllPrimeDivisorCommon(k,b)

def gcd(a,b):
    """
    The function calculates the greatest common devisor of the numbers a and b.

    Args:
        a (int): An integer
        b (int): An integer

    Returns:
        int: GCD(a,b)
    """
    r = a%b
    if (r==0):
        return b
    return gcd(b, r)

if __name__ == "__main__":
    print(gcd(3,2)==4)
    print(gcd(15,5)==10)