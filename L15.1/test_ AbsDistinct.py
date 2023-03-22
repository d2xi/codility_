import AbsDistinct

def test_countAbsDistinctValues():
    assert AbsDistinct.countAbsDistinctValues([])==0
    assert AbsDistinct.countAbsDistinctValues([20])==1
    assert AbsDistinct.countAbsDistinctValues([-20])==1

    assert AbsDistinct.countAbsDistinctValues([20,20])==1, "even len; all positive; single value;"
    assert AbsDistinct.countAbsDistinctValues([20,20,20])==1, "odd len; all positive; single value;"
    assert AbsDistinct.countAbsDistinctValues([-20,-20])==1, "even len; all negative; single value;"
    assert AbsDistinct.countAbsDistinctValues([-20,-20,-20])==1, "odd len; all negative; single value;"
    assert AbsDistinct.countAbsDistinctValues([-20,20])==1, "even len; mixed; single value;"
    assert AbsDistinct.countAbsDistinctValues([-20,20,20])==1, "odd len; mixed; single value;"
    
    assert AbsDistinct.countAbsDistinctValues([20,30])==2, "even len; all positive; mult values;"
    assert AbsDistinct.countAbsDistinctValues([20,30,30])==2, "odd len; all positive; mult values;"

    assert AbsDistinct.countAbsDistinctValues([-30,-20])==2, "even len; all negative; mult values;"
    assert AbsDistinct.countAbsDistinctValues([-30,-30,-20])==2, "even len; all negative; mult values;"

    assert AbsDistinct.countAbsDistinctValues([-10,-9,-8,-7,-6,-3,0,2,5,20,30])==11, "long seq; mixed; no dups;"
    assert AbsDistinct.countAbsDistinctValues([-10,-10,-10,-7,-6,-3,0,2,5,5,30,30])==8, "long seq; mixed; dups;"

    assert AbsDistinct.countAbsDistinctValues([-20,-20,20])==1
    assert AbsDistinct.countAbsDistinctValues([-20,-20,30])==2
    assert AbsDistinct.countAbsDistinctValues([-20,10,20])==2
    assert AbsDistinct.countAbsDistinctValues([20,30,40])==3
    assert AbsDistinct.countAbsDistinctValues([-20,30,40])==3
    assert AbsDistinct.countAbsDistinctValues([-30,-20,40])==3
    assert AbsDistinct.countAbsDistinctValues([-20,-20,-20,20,20,20])==1
    assert AbsDistinct.countAbsDistinctValues([-20,-20,30])==2
    assert AbsDistinct.countAbsDistinctValues([-20,30,30])==2
    assert AbsDistinct.countAbsDistinctValues([-20,0,20])==2
