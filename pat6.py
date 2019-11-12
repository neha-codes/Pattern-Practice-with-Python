# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:00:50 2019

@author: nehap
"""

"""
Input: 5
Output : 
* * * * * 
* * * * 
* * * 
* * 
* 

"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    print("Output :")
    for i in range(n, 0, -1):
        for j in range(0, i, 1):
            print("*", end=" ")
        print("\r")
        