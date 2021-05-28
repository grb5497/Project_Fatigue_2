import sys
sys.path.append("../project_fatigue_2")

from project_fatigue import range_overlap

def test_range_overlap():
    assert(range_overlap([(500, 10000), (0, 2000)]) == (500, 2000))
    assert(range_overlap([(200, 1000)]) == (200, 1000))

def test_range_no_overlap():
    assert(range_overlap([(10,1000),(5000,60000)]) == None)