#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:40:26 2022

@author: christopherquintas
"""

"""
-There is a var called __name__
-The module that is being ran is the main program
    - __name__ = "__main__"
-If another module is the main program that IMPORTS your module
    - import foo.py --> __name__ = "foo"

-Useful for:
    -If module is a library but you want the ability to run some main unit tests
    -You don't want some scripts running a main program when its importing somemthing
        
"""
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__': #This block only execuetes if you run the function from this foo.py
                           #Everything else always runs no matter where you call the function 
    functionA()
    functionB()
print("after __name__ guard")