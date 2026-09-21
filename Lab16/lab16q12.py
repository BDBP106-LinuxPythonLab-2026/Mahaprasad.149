"""""Write a program to check if an input string is palindrome """

word=str(input("Enter a word: "))
reverse=""
for i in range(len(word)-1,-1,-1):
    reverse=reverse+word[i]
if word==reverse:
    print("Palindromic")
else:
    print("Not a Palindromic")