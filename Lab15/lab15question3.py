#For any input integer k and another input integer n where n>0
from pygments.lexers import math

k=(int(input("Enter a number: ")))
n=(int(input("Enter a number: ")))
a=k+n
b=k-n
c=k/n
d=k*n
e=k//n
f=k**n

print('addition :' + str(a))
print('multiplication :' + str(d))
print('division :' + str(c))
print('exponentiation :' + str(f))
print('modulo/remainder :' + str(e))
print('subtraction :' + str(b))








