import MaxNonoverlappingSegments

def test_maxNumberNonoverlappingSegments():
   assert MaxNonoverlappingSegments.maxNumberNonoverlappingSegments([],[]) == 0
   assert MaxNonoverlappingSegments.maxNumberNonoverlappingSegments([1],[10]) == 1
   assert MaxNonoverlappingSegments.maxNumberNonoverlappingSegments([1,6],[5,10]) == 2
   assert MaxNonoverlappingSegments.maxNumberNonoverlappingSegments([2,3,4,5,1],[2,3,4,5,6]) == 4
   assert MaxNonoverlappingSegments.maxNumberNonoverlappingSegments([1,3,7,9,9],[5,6,8,9,10 ]) == 3
