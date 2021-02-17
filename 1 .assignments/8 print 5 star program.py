# -*- coding: utf-8 -*-
"""
8. Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *
"""
def k(no):
    for i in range(0,no):
        print("*")

def main():
    num=int(input("enter the number"))
    k(num)

if __name__=="__main__":
    main()