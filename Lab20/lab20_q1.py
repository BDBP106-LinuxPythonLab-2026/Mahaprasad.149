n=int(input("Enter a number:",))
if n >= 0:
    print("Positive no.")
    if n%2==0:
        print("even no")
    if n % 2 != 0:
        print("odd no")
if n < 0:
    print("Negative no.")
    if n % 2 == 0:
        print("even no")
    if n%2!=0:
        print("odd no")
if n%3==0 and n%5==0:
    print("FizzBuzz number!")