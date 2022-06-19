#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:32:20 2022

@author: christopherquintas
"""
import math
def binary_search(arr, left, right, key):
    
    if left > right:
        return -1
    
    mid = int(math.floor((right - left)/2))
    
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, left, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, right, key)

    


if __name__ == '__main__':    
    sorted_array = [int(i) for i in input().split()]
    key = int(input("What are you trying to find: "))
    right = len
    print(binary_search(sorted_array, 0, len(sorted_array) - 1, key))
    
    