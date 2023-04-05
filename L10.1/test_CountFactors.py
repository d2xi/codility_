import CountFactors

def test_countFactors():
    assert CountFactors.countFactors(24) == 8 
    assert CountFactors.countFactors(1) == 1 
    assert CountFactors.countFactors(2) == 2 
    assert CountFactors.countFactors(11) == 2 
    assert CountFactors.countFactors(17) == 2 
    assert CountFactors.countFactors(4) == 3