import CountTriangles

def test_countTriangles():
    assert CountTriangles.countTriangles([])==0
    assert CountTriangles.countTriangles([10,2,5,1,8,12])== 4
    assert CountTriangles.countTriangles([5,5,10])==0
    assert CountTriangles.countTriangles([5,10,20])==0
    assert CountTriangles.countTriangles([1,2,3])==0
    assert CountTriangles.countTriangles([2,3,4])==1
    assert CountTriangles.countTriangles([7,7,7])==1
    assert CountTriangles.countTriangles([7,7,7,7])==4