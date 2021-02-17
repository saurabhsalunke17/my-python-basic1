# -*- coding: utf-8 -*-
"""
Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number
"""

def primenum(no):
    for i in range(2,no):
        if (no%i)==0:
           return True
break
    else:
        return False
            
    
    
def main():
     num= int(input("enter the value"))
     k=primenum(num)
     
     if k==True:
         print("{} is not primes number ".format(num))
     else:
         print("{} is  primes ".format(num))
         
 
if __name__=="__main__":
     main()         