"""Ask for a person's age and check wheather the person is eligible to vote or not """

age=float(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")