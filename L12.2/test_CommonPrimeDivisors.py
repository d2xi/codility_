import CommonPrimeDivisors

def test_gcd():
    assert CommonPrimeDivisors.gcd(15,5) != 10
    assert CommonPrimeDivisors.gcd(15,10)==5
    assert CommonPrimeDivisors.gcd(30,10)==10
    assert CommonPrimeDivisors.gcd(13*6,8*6)==6

def test_haveAllPrimeDivisorCommon():
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2,2)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3,2*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3,2*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3,2*3*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3*3,2*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*2*3,2*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*2*3*3,2*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3,2*2*3*3)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2,3)==0
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2*3,3*2)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2**10 * 3,2 * 3**10)==1
    assert CommonPrimeDivisors.haveAllPrimeDivisorCommon(2**3 * 3**4 * 11, 2 * 3)==0

def test_countPairsWithAllPrimeDivisorsCommon():
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([],[])==0
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([1],[1])==1
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2],[3])==0
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 2], [2, 2])==2
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 3], [2, 3])==2
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 2, 3], [2, 2, 2])==2
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 2, 2], [2, 2, 2])==3
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 3, 11], [2, 3, 11])==3
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 3, 11], [2, 3, 11])==3
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2, 3, 11], [11, 2, 3])==0
    assert CommonPrimeDivisors.countPairsWithAllPrimeDivisorsCommon([2**2 * 11, 2, 3 * 11**2], [2**3 * 11**2, 2, 3**2 * 11])==3