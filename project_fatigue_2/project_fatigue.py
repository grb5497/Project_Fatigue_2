import sys
import numpy as np

def test_range_overlap():
    assert(range_overlap([(500,10000),(0,2000)]) == (500,2000))
    assert(range_overlap([(200,1000)]) == (200,1000))

def test_range_no_overlap():
    assert(range_overlap([(10,1000),(5000,60000)]) == None)

def range_overlap(ranges):
    
    #-------------------------------
    #           ---------------------------
    #       ---------------------

    max_left = max(ranges, key= lambda x: x[0])[0]
    min_right = min(ranges, key = lambda x: x[1])[1]
    
    #print(max_left, min_right)
    return (max_left, min_right)

if __name__ == '__main__':
    
    input_files = sys.argv[1:]

    list_ranges = []
    for file in input_files:
        data = np.loadtxt(file,delimiter=',')
        left_val = np.min(data[:,0])
        right_val = np.max(data[:,0])
        range_val = (left_val,right_val)
        #print (file,range_val)
        list_ranges.append(range_val)

    result = range_overlap(list_ranges)

    print("Common range: ", result)