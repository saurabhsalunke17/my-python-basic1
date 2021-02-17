# -*- coding: utf-8 -*-

"""
9. Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7
"""

def addition(arr1):
      add=0
      for i in range(0,len(arr1)):
                     add=add+1
       
      return add



def main():
     num= int(input("enter the value"))
     arr=[]
     for i in range(0,num):
         value=int(input("enter the value"))
         arr.append(value)
     k=addition(arr)   
     print(k)
     
 
if __name__=="__main__":
     main()         
    