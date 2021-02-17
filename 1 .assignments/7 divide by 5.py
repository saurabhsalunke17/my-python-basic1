# -*- coding: utf-8 -*-
"""
7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True
"""

def check(no):
    if(no%5==0):
        return True
    else:
        return False
def main():
    num=int(input("enter the number"))
    k=check(num)    
    
    if k==True:
        print("number is divide by 5 ")
    else:
        print("number is not divisible by 5")
 
if __name__=="__main__":
    main()    