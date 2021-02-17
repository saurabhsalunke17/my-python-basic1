# -*- coding: utf-8 -*-
"""
Write a program which accept one number and display below pattern.

5
Output :
* * * * *
* * * *
* * *
* *
*
"""

def pattern(no):
    for i in range(no, 0, -1):
        for j in range(0, i):
            print("*", end=' ')
        print(" ")
    
def main():
     num= int(input("enter the value"))
     pattern(num)
     
 
if __name__=="__main__":
     main()         