# -*- coding: utf-8 -*-
"""
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16
4.Write a program which display 5 times Marvellous
"""

def add(x,y):
    z=x+y
    return z
 
def main():
    no1=int(input("enter the number"))
    no2=int(input("enter the number"))
    p=add(no1,no2)
    print("addition of{} and {} is {}".format(no1,no2,p))

if __name__=="__main__":
     main()    