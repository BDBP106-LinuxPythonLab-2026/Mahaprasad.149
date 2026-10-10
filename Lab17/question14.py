""""Write a program to remove all occurrences of an element from a list, L."""

element=int(input("Enter a element you would like to find and remove: "))
L=[1,2,3,4,5,5,6,6,7,7,7,7,7,7,8,9,9,0]

while element in L:
    L.remove(element)

print(L)