# -*- coding: utf-8 -*-
"""
4.Write a program which display 5 times Marvellous on screen.
"""
def pr(num):
    i=0
    for i in range(0,num):
        print("marvellous")
def main():
    n1=int(input("enter the number"))
    pr(n1)        

if __name__=="__main__":
    main()