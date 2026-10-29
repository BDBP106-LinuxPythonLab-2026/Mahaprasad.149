sent=input("Enter a string:")
S=sent.lower()
vowels=0
consonants=0
digits=0
spaces=0
for i in S:
    if i in "aeiou":
        vowels+=1
    elif i == " ":
        spaces+=1
    elif i.isdigit():
        digits+=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        consonants += 1
print(f"Vowels:{vowels},Consonants:{consonants},Digits:{digits},Spaces:{spaces}")