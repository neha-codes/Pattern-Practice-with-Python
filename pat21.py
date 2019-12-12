# -*- coding: utf-8 -*-
"""
Created on Sun Dec 01 12:13:46 2019

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
    #Initial spaces
    k=0
    #Initialize staring number
    num = n
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n, 0, -1):
        #Inner loop - controlling blank spaces
        for j in range(0,k):
            print(end=" ")
        #Inner loop - used to print numbers
        for j in range(i,0,-1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num-1
        #Reintialize starting number for next row
        num=n   
        #Increase spaces after each row
        k=k+2
        print("\r")
    print("\r")
    #Initial spaces
    k= 2*n-2
    #Outer loop - control number of rows
    for i in range(0, n):
        #Inner loop - controlling blank spaces
        for j in range(0,k):
            print(end=" ")
        #Inner loop - used to print numbers
        for j in range (0,i+1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num-1
        #Reintialize starting number for next row
        num=n
        #Reduce spaces after each row
        k=k-2
        print("\r")