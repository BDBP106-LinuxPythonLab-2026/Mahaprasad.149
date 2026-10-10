#Write a program to find the sum of all the elements in a list using lambda and reduce functions.

from functools import reduce
a=[10, 20, 30, 40, 50]

print(reduce(lambda x,y: x+y, a))