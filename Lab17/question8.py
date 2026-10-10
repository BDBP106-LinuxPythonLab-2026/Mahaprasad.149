"""""Write a script to count the number of occurrences of a word, W, in a sentence, S."""""

s= input("Enter  a sentence: ")
W=input("Enter a word you have to count in sentence: ")

words=s.split()
count=0

for word in words:
    if word==W:
        count=count+1
print("Number of occurences:",count)

