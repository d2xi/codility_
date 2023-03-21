import ChocolatesByNumbers_naive
import ChocolatesByNumbers

def test_getNumberChocolatesEaten():
    funcs = [ChocolatesByNumbers_naive.getNumberChocolatesEaten, 
             ChocolatesByNumbers.getNumberChocolatesEaten]
    for func in funcs:
        assert func(10,1)==10
        assert func(10,2)==5
        assert func(10,4)==5
        assert func(10,4)==5

def test_gcd():
    assert ChocolatesByNumbers.gcd(15,5)==5
    assert ChocolatesByNumbers.gcd(15,10)==5
    assert ChocolatesByNumbers.gcd(30,10)==10
    assert ChocolatesByNumbers.gcd(13*6,8*6)==6