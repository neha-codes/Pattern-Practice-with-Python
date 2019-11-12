# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:21:09 2019

@author: nehap
"""

"""
Input: 5
Output :
* * * * * 
  * * * * 
    * * * 
      * *   
        * 
"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = 0
    print("Output :")
    #Outer Loop - controlling number of rows
    for i in range(n,0):
        #Inner loop - controlling blank spaces
        for j in range(i):
            print("*")
        #Inner loop - controlling stars
        #for j in range(0, i+1):
         #   print("*", end=" ")
        #reduce the spaces after each row
        k = k+2
        print("\r")
        
        
      