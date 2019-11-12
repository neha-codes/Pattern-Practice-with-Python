# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:16:21 2019

@author: nehap
"""

"""
Input: 7
Output : 1 2 3 4 5 6 7 

"""

if __name__=="__main__": 
    i =  int(input("Input: " ))
    print("Output: ", end='')
    for n in range(i):
        n+=1
        print(n, end=' ')
    