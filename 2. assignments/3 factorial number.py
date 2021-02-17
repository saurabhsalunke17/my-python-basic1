"""
Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120
"""
def factorial(no):
    fact=1
    for i in range (1,no+1):
            fact=fact*i
    return fact
def main():
      num=int(input("enter the number"))
      k=factorial(num)  
      print(k)
 
if __name__=="__main__":
     main()      