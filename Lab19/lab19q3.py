#3(a) Create a string by joining the numbers in the above list a using the comma.



a = [i for i in range(1, 51)]
A = ','.join([str(i) for i in a])
print(A)
#(b) Create a string by joining the numbers in the above list a using the period.
B='.'.join([str(i) for i in a])
print(B)
#(c) Create a string by joining the numbers in the above list a using the ‘—’.
C='-'.join([str(i) for i in a])
print(C)

#(d) Create a new string by first creating a list of squares of the elements in a, then listing them alongside the elements of a line by line. In other words,
#we want a data set that looks like 1 1 2 4  3 9. . .
d="\n".join([" ".join([str(a[i]),str(sq[i])]) for i in range(0,len(a))])
print(d)

#ii
n=["manoranjan nayak","mahima shukla",'tanishq kokate',"mahaprasad nayak","kaumudi priyadarshani","sneha bhattacharya","shravan pawale","priyanshu pradhan","aditya thakrey","parthib kalita"]
uc=[i.upper() for i in n]
print(uc)

swp=[" ".join([name.split()[1],name.split()[0]]) for name in n]
print(swp)

fl=[".".join([(p.title()).split()[0],(p.title()).split()[1]]) for p in n]
print(fl)

#iii
s="she sells sea shells that she collects from the sea floor"
longestword=[max([word for word in s.split()], key=len)]
print("The longest word is :"+str(longestword))

#iv
rw=[s.split()[i] for i in range(0,len(s.split())) for j in range((i+1),len(s.split())) if s.split()[i]==s.split()[j]]
print("The repeated words are: "+str(rw))
