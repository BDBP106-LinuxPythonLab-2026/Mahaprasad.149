#(i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.

a=[i for i in range (1,51)]
print(a)
print("(ii) Slicing with positive step:")
#(a) a[1:5]
#(b) a[3:20:2]
#c) a[::2]
#d) a[::]
#e) a[10::2]
#f) a[1:1:1]
#g) a[:0:]
#h) a[-7::1]. Is the output a non-empty list? Why did this work?
#i) a[-6:]
#j) a[-10:-4]

print(a[1:5])
print(a[3:20:2])
print(a[::2])
print(a[::])
print(a[10::2])
print(a[1:1:1])
print(a[:0:])
print(a[-7::1])
print(a[-6:])
print(a[-10:-4])

print("(iii) Slicing with negative step:")
#(a) a[::-1]
#(b) a[::-3]
#(c) a[:1:-2]
#(d) a[-1:-1:-1]
#(e) a[:-5:-1]
#(f) a[:0:-1]
#g) a[:-1:-1]
#h) a[0:-5:-1]
#i) a[-1:5:-1]
#j) a[2:2:-1]
#k) a[2:1:-1]
#l) a[0:-5]

print(a[::-1])
print(a[::-3])
print(a[:1:-2])
print(a[-1:-1:-1])
print(a[:-5:-1])
print(a[:0:-1])
print(a[:-1:-1])
print(a[0:-5:-1])
print(a[-1:5:-1])
print(a[2:2:-1])
print(a[2:1:-1])
print(a[0:-5])

#(iv) Modification of lists using list slicing:
#(a) Create a list of even numbers from a using list slicing technique.
print("Question 1(iv)(a)")
even=[i for i in a[1:50:2]]
print(even)

#(b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.
print("Question 1(iv)(b)")
b=[i for i in a[0:10]]
c=[i for i in a[35:50:2]]
b.extend(c)
print(b)
