# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:43:01 2019

@author: nehap
"""

"""
Input: 7
Output : 
* * * * * * *

"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    print("Output :")
    for i in range(n):
        print("*", end=' ')
        