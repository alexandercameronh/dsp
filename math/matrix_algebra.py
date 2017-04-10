#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 18:48:41 2017

@author: alexanderhughes
"""

import numpy as np

A=np.matrix('1,2,3;2,7,4')
B=np.matrix('1,-1;0,1')
C=np.matrix('5,-1;9,1;6,0')
D=np.matrix('3,-2,-1;1,2,3')
At=np.matrix.transpose(A)
Bt=np.matrix.transpose(B)
Ct=np.matrix.transpose(C)
Dt=np.matrix.transpose(D)
u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4])
w=np.matrix('1;8;0;5')
alpha=6


###Section 2
u+v #[ 9,  7, -4,  9]
u-v #[ 9,  7, -4,  9]
alpha*u #[ 36,  12, -18,  30]
np.dot(u,v) #51
np.linalg.norm(u) #8.6023252670426267

               
#######Section 3     
#A+C #undefined

A-Ct #[-4, -7, -3],
#        [ 3,  6,  4]])

Ct+(3*D) #[[14,  3,  3],
#        [ 2,  7,  9]]

B*A #[[-1, -5, -1],
#        [ 2,  7,  4]]

#B*At= undefined

####optional
#B*C = undefined
C*B #[[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]]
B**4 #[[ 1, -4],
#        [ 0,  1]]
A*At #[[14, 28],
#        [28, 69]]
Dt*D #[[10, -4,  0],
#       [-4,  8,  8],
#        [ 0,  8, 10]]




