# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:10:00 2019

@author: nehap
"""
"""
Input: 5
Output :
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initialize staring number
    num = 1
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n,0,-1):
        #Inner loop - used to print numbers
        for j in range(i):
            print(num, end=" ")
            num=num+1
        #Reintialize starting number for next row
        num= 6-j
        print("\r")
    print("\r")
    #Initialize staring number
    num=n  
    #Outer loop - control number of rows
    for i in range(0,n):
        #Inner loop - used to print numbers
        for j in range(0,i+1):
            print(num, end=" ")
            num=num+1
        #Reintialize starting number for next row
        num=num-(j+2)
        print("\r")
       
    

