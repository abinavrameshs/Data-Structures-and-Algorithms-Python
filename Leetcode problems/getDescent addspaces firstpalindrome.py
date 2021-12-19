# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:47:28 2021

@author: abina
"""

"""
Number of Smooth Descent Periods of a Stock

https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

Explanation : https://www.youtube.com/watch?v=YlPtmGZNIpg
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth_descents_ending_at_i =[1]*len(prices)

        for i in range(1,len(prices)) :
            if prices[i]-prices[i-1]==-1 :
                smooth_descents_ending_at_i[i] = smooth_descents_ending_at_i[i-1] + 1
        
        return sum(smooth_descents_ending_at_i)


"""
2109. Adding Spaces to a String

https://leetcode.com/problems/adding-spaces-to-a-string/

"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        list_s=list(s)
        str_modified =""
        for i in range(0,len(spaces)+1) :
            #print(i)
            if i == 0 : 
                start = 0
            else : 
                start = spaces[i-1]

            if i == len(spaces):
                end = len(s)
            else : 
                end = spaces[i]

            #print(list_s[start : end] + [" "])
            str_modified += "".join(list_s[start : end] + [" "])
        return(str_modified.rstrip())
    

"""
2108. Find First Palindromic String in the Array

https://leetcode.com/problems/find-first-palindromic-string-in-the-array/


"""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words : 
            if i == i[::-1]:
                return i
        return ""
        