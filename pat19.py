# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:00:36 2019

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
    #Initial Spaces
    k=0
    #Initialize staring number
    num = 1
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n, 0, -1):
        for j in range(k):
            print(end=" ")
        #Inner loop - used to print numbers
        for j in range(1, i+1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num+1
        #Increase the spaces after each row
        k=k+2
        #Reintialize starting number for next row
        num=num-(j-1)
        print("\r")
    print("\r")
     #Initial spaces
    k = 2*n-2
    #Initialize starting number
    num=n
    #Outer loop - control number of rows
    for i in range(0, n):
        for j in range(k):
            print(end=" ")
         #Inner loop - used to print numbers
        for j in range (0,i+1):
            print(num, end=" ")
            #Reduce value of 'num' after every value is printed
            num=num+1
        #Reintialize starting number for next row
        num=num-(j+2)
        #Decrease the spaces after each row
        k=k-2
        print("\r")
    