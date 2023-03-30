import NumberSolitaire

def test_numberSolitaire():
    assert NumberSolitaire.numberSolitaire([1,2])==3
    assert NumberSolitaire.numberSolitaire([-1,1])==0
    assert NumberSolitaire.numberSolitaire([1,-2,0,9,-1,-2])==8
    assert NumberSolitaire.numberSolitaire([0,-4,-5,-2,-7,-9,-3,-10])==-12
