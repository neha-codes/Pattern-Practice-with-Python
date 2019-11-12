# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:22:09 2019

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
    for i in range(n, 0, -1):
        #Inner loop - controlling spaces
        for j in range(k):
            print(end=" ")
        #Inner loop - controlling stars
        for j in range(i, 0, -1):
             print("*", end=" ")
        #Increment spcae after each row
        k=k+2
        print("\r")
       
        
        
        
      