# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:00:08 2019

@author: nehap
"""

"""
Input: 7
Output : 7 6 5 4 3 2 1 

"""

if __name__=="__main__": 
    i = int(input("Enter: "))
    print("Output: ", end='')
    for n in range(i,0, -1):
        print(n, end=' ')
       