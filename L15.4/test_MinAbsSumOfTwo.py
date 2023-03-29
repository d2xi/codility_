import MinAbsSumOfTwo

def test_minAbsSumOfTwo():
    assert MinAbsSumOfTwo.minAbsSumOfTwo([3,10,-200,-3])==0
    assert MinAbsSumOfTwo.minAbsSumOfTwo([1,4,-3])==1
    assert MinAbsSumOfTwo.minAbsSumOfTwo([-10,1,0,20,8,-8])==0
    assert MinAbsSumOfTwo.minAbsSumOfTwo([1000])==2000
    assert MinAbsSumOfTwo.minAbsSumOfTwo([1,2,3])==2
    assert MinAbsSumOfTwo.minAbsSumOfTwo( [-8,4,5,-10,3])==3
    assert MinAbsSumOfTwo.minAbsSumOfTwo( [-20])==40