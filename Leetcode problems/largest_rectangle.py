# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 20:14:46 2021

@author: abina

https://leetcode.com/problems/largest-rectangle-in-histogram/

Yet to find the most optimized solution
"""



class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        dict_values = {i:heights.count(i) for i in heights}
        if len(dict_values.keys())==1 :
            return list(dict_values.keys())[0]*len(heights)
        else : 
            max_area = -1
            for index, bar in enumerate(heights): 
                print("########### Number {0}".format(bar))
                # For each number, find how many are above it, beth on left side and right side.
                left = heights[:index]
                left.reverse()
                right = heights[index:]
                
                sum_area_right = 0
                sum_area_left = 0
                for x in right : 
                    if x>= bar  :
                        sum_area_right += bar
                    else : 
                        break
                
                for x in left : 
                    if x>= bar  :
                        sum_area_left += bar
                    else : 
                        break
            
                # Calculate total areas
                
                #print("total_area {0}".format(sum_area_right + sum_area_left))
                # Update max_area
                if sum_area_right + sum_area_left > max_area :
                    max_area = sum_area_right + sum_area_left
            
            return max_area

##############################################

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        dict_values = {i:heights.count(i) for i in heights}
        if len(dict_values.keys())==1 :
            return list(dict_values.keys())[0]*len(heights)
        else : 
            max_area = -1
            for index, bar in enumerate(heights): 
                #print("########### Number {0}".format(bar))
                # For each number, find how many are above it, beth on left side and right side.
                
                def map_func(x):
                    if x>=bar : 
                        return bar
                    else :
                        return 0
                    
                new_heights = list(map(map_func, heights))
                
                
                left = new_heights[:index]
                left.reverse()
                right = new_heights[index:]
                try :
                    sum_area_left = sum(left[:left.index(0)])
                except : 
                    sum_area_left = sum(left)
                
                try :
                    sum_area_right = sum(right[:right.index(0)])
                except : 
                    sum_area_right = sum(right)
                
                del left
                del right
                del new_heights
                
                # Calculate total areas
                
                #print("total_area {0}".format(sum_area_right + sum_area_left))
                # Update max_area
                if sum_area_right + sum_area_left > max_area :
                    max_area = sum_area_right + sum_area_left
            return max_area


heights = [2,1,5,6,2,3]

######## Original solution

dict_values = {i:heights.count(i) for i in heights}


max_area = -1
for index, bar in enumerate(heights): 
    print("########### Number {0}".format(bar))
    # For each number, find how many are above it, beth on left side and right side.
    left = heights[:index]
    left.reverse()
    right = heights[index:]
    print("left : ", left)
    print("right : ", right)
    
    sum_area_right = 0
    sum_area_left = 0
    for x in right : 
        if x>= bar  :
            sum_area_right += bar
        else : 
            break
    
    for x in left : 
        if x>= bar  :
            sum_area_left += bar
        else : 
            break

    # Calculate total areas
    
    #print("total_area {0}".format(sum_area_right + sum_area_left))
    # Update max_area
    print("sum_area_left ", sum_area_left)
    print("sum_area_right ", sum_area_right)
    
    if sum_area_right + sum_area_left > max_area :
        max_area = sum_area_right + sum_area_left
        
                    
###############
                   

max_area = -1
left = 0 
right = len(height)-1

while left < right :
    area_current = (right - left)* min(height[left] , height[right] )
    if area_current > max_area : 
        max_area = area_current
    
    if height[left] > height[right] : 
        right = right -1
    else : 
        left = left + 1


f5 - f4
f4-f3 - (f3-f2)
(f3-f2)-(f2-f1) - (f2-f1)+ (f1-f0)
(f2-f1)- (f1-f0)-(f1-f0) + f1 - (f1-f0) +f1 + (f1-f0)
(f1-f0-f1)- (f1-f0)-(f1-f0) + f1 - (f1-f0) +f1 + (f1-f0)

