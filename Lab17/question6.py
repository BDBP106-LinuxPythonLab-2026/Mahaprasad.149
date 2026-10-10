"""""Write print alternate characters of a string, S"""""

str=input("Enter a string: ")
for i in range(0,len(str),2):
    print(str[i],end="")