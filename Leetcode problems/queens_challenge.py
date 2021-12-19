# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:16:04 2021

@author: SUNDA29

https://leetcode.com/problems/n-queens/

Yet to find the optimal solution
"""

class Solution(object):
    def __init__(self):
        
        self.success = []
        self.success_len =[]
        self.i = 0
        self.n = None
        self.elements_to_remove = []

        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        if n==1 :
            return [0],[["Q"]]
        else : 
            for i in range(n):
                self.i = i
                self.find_next_recursive(n=n,previous_rows=[] )          
                    
            for j in self.success : 
                j.append(list(set(list(range(n))).difference(set(j))).pop())
            print("Final success", self.success)
            
            queen_result_list =[]
            for k in self.success : 
                queen_result_list.append([self.make_queen_string(j) for j in k])
        
            return self.success, queen_result_list
    
    def find_next_position_possibilities(self, n, previous_rows):
        if len(previous_rows)>n : 
            return True
        elif  len(previous_rows)>0: 
            position_previous_row = previous_rows[-1]
            position_before_prev_rows = previous_rows[:-1]
            #print("position_previous_row", position_previous_row)
            #print("position_before_prev_rows", position_before_prev_rows)
            # POsitions considered should exclude the positions before previous row and should not be within 1 square on either side of the previous row
            
            numbers_to_eliminate=[position_previous_row-1,position_previous_row, position_previous_row + 1]
            
            #print("numbers_to_eliminate", numbers_to_eliminate)
            numbers_to_eliminate.extend(position_before_prev_rows)
            #print(numbers_to_eliminate)
            list_all_positions=list(range(n))
            #print(list_all_positions)
            next_possibilities =  set(list_all_positions).difference(set(numbers_to_eliminate))
            
            print("next_possibilities", next_possibilities)
            return list(next_possibilities)
        else : 
            return True
    

    def make_queen_string(self, mark):
        string_Q = ""
        for i in range(self.n):
            if i ==mark :
                string_Q+="Q"
            else :
                string_Q+="."
        return string_Q
    
    def find_next_recursive(self, n, previous_rows):
        
        print("Initial previous_rows  ", previous_rows)
      
        if len(previous_rows) ==0 : 
            print("Entered CONDITION 1 ########## ")
            previous_rows.append(self.i)
            #print("previous_rows inside if ", previous_rows)
            self.find_next_recursive(n = n,previous_rows = previous_rows)
        else :
            print("Entered CONDITION 2 ########## ")
            #print("previous_rows inside else ", previous_rows)
            next_possibilities=self.find_next_position_possibilities(n = n, previous_rows =previous_rows )
            #print(len(next_possibilities))
            if len(next_possibilities)!=0:
                print("Entered CONDITION 3 ########## ")
                previous_rows.append(next_possibilities[0])
               
                if len(previous_rows) == n : 
                    if abs(previous_rows[-1]-previous_rows[0])!=n :
                        print("SUCCESS !!!")
                        print(previous_rows)
                        
                        self.success.append(previous_rows)
                        
                        print("success : ", self.success)
                        self.success_len.append(len(previous_rows))
                
                self.find_next_recursive(n = n,previous_rows = previous_rows)
            else :
                print("Entered CONDITION 4 ########## ")
                try : 
                    # pop the last element in previous_rows
                    popped_element=previous_rows.pop()
                    self.elements_to_remove.append(popped_element)
                    next_possibilities=self.find_next_position_possibilities(n = n, previous_rows =previous_rows )
                    # remove popped_element from next_possibilities
                    for ele in self.elements_to_remove : 
                        next_possibilities.remove(ele)
                    
                    if len(next_possibilities)>0 :
                        print("Entered CONDITION 5 ########## ")
                        previous_rows.append(next_possibilities[0])
                        self.find_next_recursive(n,previous_rows)
                        self.elements_to_remove=[]
                except : 
                    print("Nothing to do ")
          
            

#sol_obj = Solution()
result_placements, result_queens = Solution().solveNQueens(n =1)
print(result_placements)
print(result_queens)
