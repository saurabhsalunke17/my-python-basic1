# -*- coding: utf-8 -*-
"""
Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6
"""

def factors(no):
    x=0
    for i in range(1,no):
        if(no%i==0):
            x=x+i
            print(i)
    return x   
    
def main():
     num= int(input("enter the value"))
     k=factors(num)
     print("factors of {} is as fallows {} ".format(num,k))
 
if __name__=="__main__":
     main()     