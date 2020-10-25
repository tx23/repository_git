#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author  : exiahan@exiahan.com
# @Time    : 2020/03/26
# @File    : z3_test.py


import z3

# Find Solution Set That Can Make Logical Expression P/\Q be True
P, Q = z3.Bools('P Q')
F = z3.And(P, Q)
solver = z3.Solver()
solver.add(F)
print(solver.check())
print(solver.model())
