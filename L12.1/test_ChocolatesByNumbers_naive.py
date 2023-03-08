import ChocolatesByNumbers_naive

def test_getNumberChocolatesEaten():
    assert ChocolatesByNumbers_naive.getNumberChocolatesEaten(10,1)==10
    assert ChocolatesByNumbers_naive.getNumberChocolatesEaten(10,2)==5
    assert ChocolatesByNumbers_naive.getNumberChocolatesEaten(10,4)==5
    assert ChocolatesByNumbers_naive.getNumberChocolatesEaten(10,4)==5