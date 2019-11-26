# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:22:09 2019

@author: nehap
"""

"""
Input: 5
Output :
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
if __name__=="__main__": 
    n =  int(input("Input: "))
    #Initial spaces
    k = n-1
    print("Output :")
    #Outer Loop - controlling number of rows
    for i in range(0, n, 1):
        #Inner loop - controlling spaces
        for j in range(0,k):
            print(end=" ")
        #Inner loop - controlling stars
        for j in range(0,i+1):
             print("*", end=" ")
        #Increment spcae after each row
        k=k-1
        print("\r")
       
        
        
        
      