# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:03:41 2019

@author: nehap
"""
"""
Input: 5
Output :
5 4 3 2 1 
5 4 3 2 
5 4 3
5 4 
5

5
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1
 
"""

if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initialize staring number
    num = n
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n, 0, -1):
        #Inner loop - used to print numbers
        for j in range(i,0,-1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num-1
        #Reintialize starting number for next row
        num=n
        print("\r")
    print("\r")
    #Outer loop - control number of rows
    for i in range(0, n):
         #Inner loop - used to print numbers
        for j in range (0,i+1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num-1
        #Reintialize starting number for next row
        num=n
        print("\r")
    