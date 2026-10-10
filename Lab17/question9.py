"""Write a script to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams"""

S1=input("Enter first string: ")
S2=input("Enter second string: ")

if sorted(S1)== sorted(S2):
    print("Anagram")
else:
    print("Not Anagram")