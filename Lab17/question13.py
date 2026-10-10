""""Write a program to extract elements of a list, if it occurs more than k times."""""

L = [1, 3, 5, 3, 2, 3, 5, 5, 4, 3, 1, 5, 5]
k=int(input("Enter the number of occurrences: "))
result=[]
for i in L:
    if L.count(i)>k and i not in result:
        result.append(i)
print("The duplicate elements that occur more than k times are: ", result)
