# ratio_merge
*A small utility function for merging two python lists by some ratio*

This function acts as a generator producing elements from the two given lists by the given `<merge_ratio>`.
The generator would preserve any internal order within the lists and would produce no more then 
`<desired_length>` elements in total.

In case the total number of elements within either list is not enough to maintain the desired ratio
throughout, the function would continue to generate elements from the remaining set until `<desired_length>` 
elements were produced.

If the `<strict>` parameter is set to True the function will stop producing elements once one of the lists has
ran out of elemets. It whould also bias the produced list to fit closest to the length of the `<first_list>`.

## Install
1. `pip install ratio_merge`
2. ?????
3. profit

## Usage Examples:
```
    ~$ python
	>>> from ratio_merge import ratio_merge
	>>>
	>>> x=[1,2,3,4,5]
	>>> y=['a','b','c','d','e','f','g']
	>>>
	>>> l = ratio_merge(x,y, 0.7) # <- evaluates on the fly
	>>> l
		<generator object ratio_merge at 0x7fd93902d870>
	>>> list(l)
		[1, 'a', 2, 3, 'b', 4, 5, 'c', 'd', 'e']
	>>>
	>>> l = ratio_merge(x,y, 0.7, 5) # <- length limit
	>>> list(l)
		[1, 'a', 2, 3, 'b']
	>>>
	>>> l = ratio_merge(x,y, 0.2) # <- differant ratio
	>>> list(l)
		[1, 'a', 'b', 'c', 'd', 2, 'e', 3, 4, 5]
	>>>
	>>>
	>>> l = ratio_merge(x,y, 0.5) # <- replicates zip order on 0.5
	>>> list(l)
		[1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']
	>>> zip(x,y)
		[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

```
