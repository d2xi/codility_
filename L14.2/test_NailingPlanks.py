import NailingPlanks

def test_getIdLeftMostNalingPosition():
    assert NailingPlanks.getIdLeftMostNalingPosition(0,5,[(5,0)])==0
    assert NailingPlanks.getIdLeftMostNalingPosition(0,5,[(0,5)])==0
    assert NailingPlanks.getIdLeftMostNalingPosition(4,5,[(0,0),(1,4)])==1
    assert NailingPlanks.getIdLeftMostNalingPosition(4,5,[(0,0),(1,5)])==1
    assert NailingPlanks.getIdLeftMostNalingPosition(4,10,[(4,1),(1,2),(3,3),(0,10)])==3
    assert NailingPlanks.getIdLeftMostNalingPosition(4,10,[(1,3),(0,2)])==-1
    assert NailingPlanks.getIdLeftMostNalingPosition(4,10,[(1,1),(2,2),(3,3),(4,4),(0,5)])==3

def test_getEarliestNalingPosition():
    assert NailingPlanks.getEarliestNalingPosition(1,5,[(3,0),(2,2),(4,4),(1,5)])==3
    assert NailingPlanks.getEarliestNalingPosition(0,2,[(1,0),(0,3),(2,4),(3,6),(4,10)])==0
    assert NailingPlanks.getEarliestNalingPosition(0,2,[(1,0),(0,2),(2,4),(3,6),(4,10)])==1
    assert NailingPlanks.getEarliestNalingPosition(1,5,[(0,1),(4,2),(3,3),(2,4),(1,5)])==4

def test_getMinNumberNails():
    assert NailingPlanks.getMinNumberNails([1],[2],[3])==-1
    assert NailingPlanks.getMinNumberNails([1],[2],[1])==1
    assert NailingPlanks.getMinNumberNails([1,2],[2,3],[2])==1
    assert NailingPlanks.getMinNumberNails([1,2],[2,3],[1,2])==2
    assert NailingPlanks.getMinNumberNails([1,4,5,8],[4,5,9,10],[4,6,7,10,2])==4
    assert NailingPlanks.getMinNumberNails([1,2,3,6],[4,5,6,10],[4,6])==2
    assert NailingPlanks.getMinNumberNails([1,2,3,6],[4,5,6,10],[1,2,3,6,4])==4
    assert NailingPlanks.getMinNumberNails([1,2,3,6],[4,5,6,10],[1,2,3,4,6])==5
    assert NailingPlanks.getMinNumberNails([1,2],[4,3],[2,1])==1
    assert NailingPlanks.getMinNumberNails([2],[5],[0,1,6,7,8,9,10,2])==8
    assert NailingPlanks.getMinNumberNails([2],[5],[0,1,6,2,8,9,10])==4
    assert NailingPlanks.getMinNumberNails([1,6],[5,9],[0,1,2,3,4,5,6,9,5])==7
    assert NailingPlanks.getMinNumberNails([1,3],[4,20],[0,1,4,20])==3
    assert NailingPlanks.getMinNumberNails([1,10],[3,20],[0,1,5,6,7,20])==6

