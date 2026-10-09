#(2) Lists and do loops
#(i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.

a=[i for i in range (1,51)]
Total=sum([i for i in a])
print(Total)

#(ii) Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b=[i for i in range(2,51) if all(i % n !=0 for n in range(2,i))]
print(b)

c=[j for i in a for j in b if j==i]
print(c)





