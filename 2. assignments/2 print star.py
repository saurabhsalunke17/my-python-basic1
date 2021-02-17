# -*- coding: utf-8 -*-
"""
Write a program which accept one number and display below pattern.
Input : 5
"""

def printing(no):
    for i  in range(0,no):
        for i in range(0,no):
            print("*",end='')
        print()
                
   
def main():
      num=int(input("enter the number"))
      printing(num)    
 
if __name__=="__main__":
     main()      