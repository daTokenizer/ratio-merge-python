# ratio-merge-python
*A small utility function for merging two python lists by some ratio*

This function acts as a generator producing elements from the two given lists by the given `<merge_ratio>`.
The generator would preserve any internal order within the lists and would produce no more then 
`<desired_length>` elements in total.

In case the total number of elements withing either the lists is not enough to maintain the desired ratio
throughout, the function would continue to generate elements from the remaining set until `<desired_length>` 
elements were produced.

If the `<strict>` parameter is set to True the function will stop producing elements once one of the lists has
ran out of elemets. It whould also bias the produced list to fit closest to the length of the `<first_list>`.

## Usage Examples:
```
~$ python
	>>> from ratio_merge import ratio_merge
	>>> x=[1,2,3,4,5]
	>>> y=['a','b','c','d','e']
	>>> ratio_merge(x,y,0.6,5)
		<generator object ratio_merge at 0x7fd93902d870>
	>>> list(ratio_merge(x,y,0.6,5))
		[1, 'a', 2, 'b', 3]
	>>> list(ratio_merge(x,y,0.4,5))
		[1, 'a', 'b', 2, 'c']
```