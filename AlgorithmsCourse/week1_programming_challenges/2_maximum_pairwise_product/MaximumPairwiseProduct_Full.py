#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:27:05 2022

@author: christopherquintas
"""
import numpy as np

def MaxPairwiseProductSlow(numbers):
    n = len(numbers)
    result = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]
    return result

def MaxPairwiseProductFast(numbers):
    n = len(numbers)
    product = 0
    for i in range(0,n):
        for j in range(i+1,n):
            product = max(product, numbers[i] * numbers[j])
    return product

def MaxPairwiseProductFastest(numbers):
    n = len(numbers)
    index_1 = 0
    for i in range(1,n-1):   #Scan for max
        if numbers[i]>numbers[index_1]:
            index_1 = i   
             
    if index_1 == 0: #Ensures that if max is at i = 0, there isn't an issue
        index_2 = 1
    else:
        index_2 = 0  
    
    for i in range(1,n-1):
        if numbers[i] != numbers[index_1] & numbers[i] > numbers[index_2]:
            index_2 = i
    product = numbers[index_1]*numbers[index_2]
    return product
 

def MaxPairwiseProductMyOwnSolution(numbers):
    product = 0
    tmplist = np.unique(numbers)
    n = len(tmplist)
    product = tmplist[n-1]*tmplist[n-2]
    return product


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(MaxPairwiseProductSlow(input_numbers))
    print(MaxPairwiseProductFast(input_numbers))
    print(MaxPairwiseProductMyOwnSolution(input_numbers))
    print(MaxPairwiseProductFastest(input_numbers))