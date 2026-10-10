#Write a program to concatenate a list of strings to make a sentence using reduce function.

from functools import reduce


words =["My","name", "is", "Mahaprasad", "Nayak"]

sentence = reduce(lambda x, y: x + " " + y, words)

print(sentence)