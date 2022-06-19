#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:57:21 2022

@author: christopherquintas
"""

import random
import numpy as np


def BinarySearch(A,low, high,key):
    if high < low:  #if it is an empty array
        return low - 1
    mid = (low + (high - low)/2)
    mid = int(np.floor(mid))
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A, low, mid-1, key)
    else:
        return BinarySearch(A, mid+1, high, key)
    

n = int(input('How long of a list: '))
lower, upper = map(int, input("Enter upper and lower bounds: ").split())
key = int(input("What are you trying to find: " ))
Arr = random.sample(range(lower,upper),n)
Arr.sort()
print(BinarySearch(Arr, lower, n, key))

    


