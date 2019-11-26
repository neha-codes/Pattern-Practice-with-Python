# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:04:07 2019

@author: nehap
"""
"""
Input: 5
Output :
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initialize staring number
    num =1
    print("Output :")
    #Outer loop - control number of rows
    for i in range(0, n):
       #Inner loop - prints numbers in each row
       for j in range(0, i+1):
           print(num, end=" ")
           num=num+1
       #Reintialize starting number for next line
       num=1
       print("\r")
    
