"""Write a program to print the duplicate elements in a list, L."""
L=[2,2,2,3,4,6,6,9,0,8,9,5,4,1,5,6]
duplicates=[]
for i in L:
    if L.count(i) > 1 and i not in duplicates:    #matlab no. mera ek se jyada ho aur voh duplicate list mein naa ho
        duplicates.append(i)

print("Duplicates elements are in list(L):",duplicates)