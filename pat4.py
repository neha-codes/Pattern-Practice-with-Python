# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:00:01 2019

@author: nehap
"""

"""
Input: 5
Output : 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    print("Output :")
    for i in range(0, n, 1):
        for j in range(n,0, -1):
            print("*", end=" ")
        print("\r")
        