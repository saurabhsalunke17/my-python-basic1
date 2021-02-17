# -*- coding: utf-8 -*-
"""
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"""

def add(x,y):
    z=x+y
    return z

def sub(m,n):
    z=m-n
    return z

def mul(m,n):
    z=m*n
    return z

def div(m,n):
    z=m/n
    return z
 
def main():
    no1=int(input("enter the number"))
    no2=int(input("enter the number"))
    p=add(no1,no2)
    print("addition of{} and {} is {}".format(no1,no2,p))
    p=sub(no1,no2)
    print("substraction of{} and {} is {}".format(no1,no2,p))
    p=mul(no1,no2)
    print("multiplication of{} and {} is {}".format(no1,no2,p))
    p=div(no1,no2)
    print("division of{} and {} is {}".format(no1,no2,p))
    
if __name__=="__main__":
     main()    