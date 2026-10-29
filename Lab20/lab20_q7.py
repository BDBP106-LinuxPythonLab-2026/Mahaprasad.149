# 7. Word Frequency Counter
# Concepts: dictionaries, split(), strip(), lower(), get(), items()
# Read a paragraph. Count how often each word appears, ignoring case and stripping
# surrounding punctuation (.,!?;:). Print the words alphabetically with their counts.
P=input("Enter a paragraph:",)
words=P.split()
count={}
for word in words:
    word=word.strip(".,!?;:").lower()
    if word!="":
        count[word]=count.get(word,0)+1
for word,n in sorted(count.items()):
    print(word,n)
highest=0
for word,n in count.items():
    if n>highest:
        highest=n
print("Most frequent word:",)
for word,n in count.items():
    if n==highest:
        print(word)