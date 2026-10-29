
# Concepts: sets, set operations, converting lists to sets, len()
# python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
# java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
# Remove the duplicates, then print:
# • students taking both courses
# • students taking only Python
# • students taking exactly one course
# • every unique student, in sorted order
# Finally, ask for a name and say which course(s) that student is enrolled in.
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
PS=set(python_class)
JS=set(java_class)

print("Both courses students:", sorted(PS & JS))
print("Only Python courses students:", sorted(PS - JS))
print("One courses students:", sorted(PS ^ JS))
print("Every students:", sorted(PS | JS))
n= input("Enter a name:",)
if n in PS and JS:
    print("Both Python and Java")
elif n in PS:
    print("Only Python")
elif n in JS:
    print("Only java")
else:
    print("Not Enrolled")