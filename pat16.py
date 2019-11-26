# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:03:41 2019

@author: nehap
"""
"""
Input: 5
Output :
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""

if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = 0
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n, 0, -1):
        #Innrer loop - used to print numbers
        for j in range(i,0,-1):
            print(j, end=" ")
        #Increment space after each row
        k=k+2
        print("\r")
    #Outer loop - control number of rows    
    for i in range(0,n+1,1):
        #Innrer loop - used to print numbers
        for j in range(i, 0, -1):
            print(j, end=" ")
        print("\r")
    