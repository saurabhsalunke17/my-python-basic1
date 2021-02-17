# -*- coding: utf-8 -*-
"""
6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
"""
def check(no):
    if(no>0):
        return True
    elif(no==0):
        print("number  is 0")
    
    else:
        return False
    
def main():
    num=int(input("enter the number"))
    k=check(num)
    if k==True:
        print("number is positive")
    else:
        print("number is not positive")
        
if __name__=="__main__":
    main()        
