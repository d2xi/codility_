import CountDistinctSlices

def test_countDistinctSlices():
    assert CountDistinctSlices.countDistinctSlices([]) == 0
    assert CountDistinctSlices.countDistinctSlices([1]) == 1
    assert CountDistinctSlices.countDistinctSlices([1,2]) == 3
    assert CountDistinctSlices.countDistinctSlices([1,2,1]) == 5
    assert CountDistinctSlices.countDistinctSlices([3, 4, 5, 5, 2]) == 9