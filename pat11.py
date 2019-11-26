# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:28:11 2019

@author: nehap
"""

"""
Generate 1 to 10 tables
"""

if __name__=="__main__": 
    n=10
    print("Output:")
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j, end="  ")
        print("\r")