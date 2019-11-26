# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:51:55 2019

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
   #Initial Spaces
   k=n-1
   print("Output :")
   #Outer loop - controlling number of rows
   for i in range(n, 0, -1):
       #Inner loop - controlling spaces
       for j in range(i, n, 1):
           print(end=" ")
        #Inner loop - prints stars 
       for j in range(0, i, 1):
           print("*", end=" ")
       k=k-1
       print("\r")
        
        
        
        