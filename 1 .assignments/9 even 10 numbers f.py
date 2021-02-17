# -*- coding: utf-8 -*-
"""
Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
"""
def evenno(no):
    for i in range(1,no):
        if i%2==0:
            print(i)

def main():
    num=int(input("enter the number"))
    evenno(num)

if __name__=="__main__":
    main()

