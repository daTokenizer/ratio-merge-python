def ratio_merge(first_list, second_list, merge_ratio=0.5, desired_length=None):
    # This function acts as a generator producing elements from the two given lists by the given <merge_ratio>.
    # The generator would preserve any internal order within the lists and would produce no more then 
    # <desired_length> elements in total.
    # In case the total number of elements withing either the lists is not enough to maintain the desired ratio
    # throughout, the function would continue to generate elements from the remaining set until <desired_length> 
    # elements were produced.
    current_ratio = 0.0
    current_length = 0
    first_list_pop_count = 0
    second_list_pop_count = 0

    combined_list_length = len(first_list) + len(second_list)
    if desired_length is None or desired_length > combined_list_length:
        desired_length = combined_list_length

    try:
        while current_length < desired_length:
            if current_ratio <= merge_ratio:
                yield first_list[first_list_pop_count]
                first_list_pop_count += 1
            else:
                yield second_list[second_list_pop_count]
                second_list_pop_count += 1
            current_length += 1
            current_ratio = float(first_list_pop_count) / current_length

    except IndexError:
        lst, lst_count = (first_list, first_list_pop_count) if first_list_pop_count < len(first_list) else (second_list, second_list_pop_count)
        try:
            while current_length < desired_length:
                yield lst[lst_count]
                lst_count += 1
                current_length += 1

        except IndexError:
            return

def test_print(actual, expected):
    return 'PASS' if cmp(actual, expected)==0 else 'FAIL. \n Expected: {}\n Got:      {}'.format(expected, actual) 


def run_tests():
    from itertools import chain
    x = [1,2,3,4,5,6,7,8,9,0]
    y = ['a','b','c','d','e','f','g','h','i','j']
    print 'compare to zip (flattened) :', test_print(list(ratio_merge(x,y)),list(chain(*zip(x,y))))

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
    print '70:30 ratio (limited to 10, but only 3 elements in first list):', test_print(list(ratio_merge(x[:3],y,0.7,10)), [1, 'a', 2, 3, 'b', 'c', 'd', 'e', 'f', 'g'])

run_tests()
