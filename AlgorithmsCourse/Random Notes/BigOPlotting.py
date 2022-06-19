#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:22:28 2022

@author: christopherquintas
"""

import matplotlib.pyplot as plt
import numpy as np


n = np.linspace(1, 100)
plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
plt.plot(n, 7 * n * n, label="7n^2")
plt.legend(loc='upper left')
plt.show()


a = int(input())
plt.plot(n,a * np.log(n), label = "log(n)")
plt.plot(n,a * np.sqrt(n),label = "sqrt(n)")
plt.plot(n,a * n,label = "n")
plt.plot(n,a * n * np.log(n),label = "n*log(n)")
plt.plot(n,a * n ** 2,label = "n^2")
plt.plot(n,a * n ** 3,label = "n^3")
plt.plot(n,a**n,label = "a^n")
plt.legend(loc = 'upper left')
plt.show()
