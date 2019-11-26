# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:14:29 2019

@author: nehap
"""

"""
Input: 5
Output :
        1
      2 1
    3 2 1
  4 3 2 1  
5 4 3 2 1
"""

if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = 2*n-2
    print("Output :")
    #Outer Loop - controlling number of rows
    for i in range(0, n):
        #Inner loop - controlling blank spaces
        for j in range(0, k):
            print(end=" ")
        #Inner loop - Printing pattern
        for j in range(i+1, 0, -1):
          print(j, end=" ")
        #reduce the spaces after each row/
        k=k-2
        print("\r")
    
