from ratio_merge.ratio_merge import ratio_merge

def test_print(actual, expected):
    return 'PASS' if cmp(actual, expected)==0 else 'FAIL. \n Expected: {}\n Got:      {}'.format(expected, actual) 


def run_tests():
    from itertools import chain
    x = [1,2,3,4,5,6,7,8,9,0]
    y = ['a','b','c','d','e','f','g','h','i','j']
    print 'compare to (flattened) zip:', test_print(list(ratio_merge(x,y)),list(chain(*zip(x,y))))

    print '75:25 ratio (limited to 10):',  test_print(list(ratio_merge(x,y,0.75,10)), [1, 'a', 2, 3, 4, 'b', 5, 6, 7, 'c'])
    print '25:75 ratio (limited to 10):', test_print(list(ratio_merge(x,y,0.25,10)), [1, 'a', 'b', 'c', 2, 'd', 'e', 'f', 3, 'g'])
    print '70:30 ratio (limited to 10):', test_print(list(ratio_merge(x,y,0.7,10)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6, 7])
    print '30:70 ratio (limited to 10):', test_print(list(ratio_merge(x,y,0.3,10)), [1, 'a', 'b', 'c', 2, 'd', 'e', 3, 'f', 'g'])
    print '70:30 ratio (limited to 9):', test_print(list(ratio_merge(x,y,0.7,9)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6])
    print '70:30 ratio (limited to 10):', test_print(list(ratio_merge(x,y,0.7,10)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6, 7])
    print '70:30 ratio (limited to 11):', test_print(list(ratio_merge(x,y,0.7,11)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6, 7, 8])
    print '70:30 ratio (unlimited):', test_print(list(ratio_merge(x,y,0.7)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6, 7, 8, 'd', 9, 0, 'e', 'f', 'g', 'h', 'i', 'j'])
    print '70:30 ratio (unlimited, but only 3 elements in second list):', test_print(list(ratio_merge(x,y[:3],0.7)), [1, 'a', 2, 3, 'b', 4, 5, 'c', 6, 7, 8, 9, 0])
    print '70:30 ratio (unlimited, but only 3 elements in first list):', test_print(list(ratio_merge(x[:3],y,0.7)), [1, 'a', 2, 3, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print '70:30 ratio (unlimited, but only 3 elements in first list and strict):', test_print(list(ratio_merge(x[:3],y,0.7,strict=True)), [1, 'a', 2, 3])
    print '75:25 ratio (unlimited, but only 3 elements in first list and strict):', test_print(list(ratio_merge(x[:3],y,0.7,strict=True)), [1, 'a', 2, 3])
    print '70:30 ratio (limited to 10, but only 3 elements in first list):', test_print(list(ratio_merge(x[:3],y,0.7,10)), [1, 'a', 2, 3, 'b', 'c', 'd', 'e', 'f', 'g'])


run_tests()
