# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:30:25 2019

@author: nehap
"""
"""
Input: 5
Output :
* 
* *
* * * 
* * * * 
* * * * * 
* * * *
* * *
* * 
*

"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    print("Output :")
    #Outer loop - control number of rows
    for i in range(0,n):
        #Inner loop - used to print numbers
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")
    #Outer loop - control number of rows
    for i in range(n,0,-1):
        #Inner loop - used to print numbers
        for j in range(0,i-1):
            print("*", end=" ")
        print("\r")
     