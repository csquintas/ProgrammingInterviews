#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:03:58 2022

@author: christopherquintas
"""

def EuclidGCD(a,b):
    if b == 0:
        return a
    a_prime = a % b
    return EuclidGCD(b,a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split())
    ans = EuclidGCD(a, b)
    print(ans)
    