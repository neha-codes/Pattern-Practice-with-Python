# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:05:57 2019

@author: nehap
"""
"""
Input: 5
Output :
1 2 3 4 5 
  1 2 3 4
    1 2 3 
      1 2
        1
        
        1
      1 2 
    1 2 3
  1 2 3 4
1 2 3 4 5 
"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = 0
    #Initialize staring number
    num =1
    print("Output :")
    #Outer loop - control number of rows
    for i in range(n,0, -1):
       #Inner loop - controlling blank spaces
       for j in range (0,k):
           print(end=" ")
       #Inner loop - prints numbers in each row
       for j in range(0, i):
           print(num, end=" ")
           num=num+1
       #Reintialize starting number for next line
       num=1
       #Increase the spaces after each row
       k=k+2
       print("\r")
    print("\r")
    #Initial spaces
    k = 2*n-2
    #Outer loop - control number of rows
    for i in range(0,n):
       #Inner loop - controlling blank spaces
       for j in range (0,k):
           print(end=" ")
       #Inner loop - prints numbers in each row
       for j in range(0, i+1):
           print(num, end=" ")
           num=num+1
       #Reintialize starting number for next line
       num=1
       #reduce the spaces after each row/
       k=k-2
       print("\r")
      

    
