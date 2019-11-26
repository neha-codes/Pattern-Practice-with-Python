# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:03:41 2019

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
"""

if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = 0
    print("Output :")
    #Outer Loop - controlling number of rows
    for i in range(n,0, -1):
        #Inner loop - controlling blank spaces
        for j in range(k):
            print(end=" ")
        #Inner loop - Printing pattern
        for j in range(i, 0, -1):
          print(j, end=" ")
        #reduce the spaces after each row
        k=k+2
        print("\r")
    
