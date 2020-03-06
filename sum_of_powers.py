#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:01:53 2020

@author: Tarik Hoshan
"""

from sympy.matrices import Matrix
from sympy.polys.polytools import Poly
from sympy import factor


k = 6 # power
matrix = []
c = []
s = 0
for n in range(k+1):
    row = []
    for i in range(k+1):
        row.append((n+1)**(i+1))

    matrix.append(row)  
    s += (n+1)**k
    c.append(s)
    
matrix = Matrix(matrix)
c = Matrix(c)
#print(matrix)
#print(c)

invmat = matrix.inv() 
r = invmat * c
print('Formula for sum of powers of %d:' % k)
poly = 0
from sympy.abc import n
for i in range(k+1):
    poly += (r[i])*n**(i+1)
poly = factor(poly)
print(poly)

n = 6

print('Sum of powers of %d from 1 to %d calculated through looping:' % (k, n))
f = lambda n : sum(((i+1)**k for i in range(n)))
print(f(6))

print('Sum of powers of %d from 1 to %d calculated with the formula:' % (k, n))
s = Poly(poly).eval(n)
print(s)


    