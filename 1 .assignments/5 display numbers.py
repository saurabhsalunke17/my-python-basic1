# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:13:26 2021

@author: shree
"""

def mydata():
    i=10
    print("in fun")
    for i in range(10 ,0,-1):
        print(i)
    
    
def main():
    print("in main()")
    mydata()    
    
if __name__=="__main__":
    main()   