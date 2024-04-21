'''
Program to find L and U matrix using LU decomposition.
Developed by: HIRUTHIK SUDHAKAR
RegisterNumber: 212223240054
'''
import numpy as np
from scipy.linalg import lu
A=np.array(eval(input()))
P,L,U=lu(A)
print(L)
print(U)

'''Program to solve a matrix using LU decomposition.
Developed by: HIRUTHIK SUDHAKAR
RegisterNumber: 212223240054
'''
# To print X matrix (solution to the equations)
import numpy as np
from scipy.linalg import lu_factor,lu_solve
A=np.array(eval(input()))
B=np.array(eval(input()))
lu,piv=lu_factor(A)
x=lu_solve((lu,piv),B)
print(x)