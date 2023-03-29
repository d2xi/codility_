import Dominator

def test_getIndexOfDominator():
    assert Dominator.getIndexOfDominator([3,4,3,2,3,-1,3,3]) in [0,2,4,6,7]
    assert Dominator.getIndexOfDominator([1,2,1]) in [0,2]
    assert Dominator.getIndexOfDominator([2,2,3,3]) == -1

def test_countOccurence():
    assert Dominator.countOccurence(1,[1,2,1]) == 2
    assert Dominator.countOccurence(0,[1,2,1]) == 0