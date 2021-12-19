# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:44:00 2021

@author: abina
"""

##### 
"""


https://leetcode.com/problems/sum-of-subarray-ranges/
"""

nums =  [4,-2,-3,4,1]
sum_subarray_range = [0]*len(nums)
max_subarray_range  = nums
min_subarray_range  = nums

1 
sum_subarray_range = 0
max_subarray_range  = 1
min_subarray_range  = 1

4
4 1 

max_subarray_range = max(4, max_subarray_range[1]) =  4
min_subarray = min(4, max_subarray_range[1]) =  1
sum_subarray_range = 0 + (4-1) = 3

-3 = 0
-3 4 = 7
-3 1 = 4
-3 4 1 = 7

max_subarray_range = max(-3, max_subarray_range[4]) =  4
min_subarray = min(-3, max_subarray_range[4]) =  -3
sum_subarray_range = 0 + (4-1) = 3

max_subarray = max(-3, max_subarray[4])
min_subarray = min(-3, min_subarray[4])
sum_subarray = max_subarray - min_subarray = 4-(-3) = 7

-2
-2 -3
-2 4
-2 1
-2 -3 4
-2 -3 1


sum_subarray = 0
for left in range(len(nums)):
    for right in range(left+1,len(nums)-1 ):
        sum_subarray += max(nums[left:right]) - min(nums[left:right])

