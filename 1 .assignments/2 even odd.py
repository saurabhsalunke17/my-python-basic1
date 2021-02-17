# -*- coding: utf-8 -*-
"""
Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11 Output : Odd Number
Input : 8 Output : Even Number
"""

def chknum(no):
    if(no%2==0):
        return True
    else:
        return False


def main():
     num=int(input("enter the number")) 
     v = chknum(num)
     if(v==True):
         print("number is even")
     else:
         print("number is odd")
         
if __name__=="__main__":
      main()         
         