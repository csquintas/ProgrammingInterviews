#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:29:19 2022

@author: christopherquintas
"""
import random as random
import numpy as np

def StressTest(N,M):
    
    a = 1
    while a == 1:
        n = random.randint(2,N)
        numbers = np.zeros((n),dtype = int)
        for i in range(0,n):
            numbers[i] = random.randint(0,M)
        print(numbers)
        result_1 = MaxPairwiseProductSlow(numbers)
        result_2 = MaxPairwiseProductFast(numbers)
        if result_1 == result_2:
            print('Success')
        else:
            print("Wrong Answer: ",result_1,result_2)
            

def MaxPairwiseProductFast(numbers):
    n = len(numbers)
    index_1 = 0
    for i in range(1,n):   #Scan for max
        if numbers[i]>numbers[index_1]:
            index_1 = i   
             
    if index_1 == 0: #Ensures that if max is at i = 0, there isn't an issue
        index_2 = 1
    else:
        index_2 = 0  
    
    for i in range(0,n):
        if ((numbers[i] != numbers[index_1]) & (numbers[i] > numbers[index_2])):
            index_2 = i
    product = numbers[index_1]*numbers[index_2]
    return product

def MaxPairwiseProductSlow(numbers):
    n = len(numbers)
    result = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]
    return result

StressTest(20,30)
    