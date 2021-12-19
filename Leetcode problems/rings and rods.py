# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:37:31 2021

@author: abina
https://leetcode.com/contest/weekly-contest-271/problems/rings-and-rods/


"""

rings = "B0B6G0R6R0R6G9"
colors = []
positions = []
for index, string in enumerate(rings): 
    if index % 2 ==0 : 
        colors.append(string)
    else : 
        positions.append(string)

dict_positions ={}
#dict_positions.keys = list(set(positions))        
for color, pos in zip(colors, positions):
    if pos not in dict_positions.keys():
        dict_positions[pos] = []
        dict_positions[pos].append(color)
    else : 
        dict_positions[pos].append(color)


count_rings = 0
for key, value in dict_positions.items():
    found_key = 0
    for i in ['R','G','B']:
        found_key += int(i in value)
    if found_key ==3 : 
        count_rings +=1
        
        

