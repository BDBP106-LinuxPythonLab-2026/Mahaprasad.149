""""Find roots of a quadratic equation. """

a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
c=float(input("Enter another number: "))

D=b**2-4*a*c
if (D<0):
    print("Discriminant is negative, so no rootes found ")
    print("discriminant is {d} ")

else:

    root1=(-b+(((b**2)-(4*a*c))**(1/2)))/(2*a)
    root2=(-b-(((b**2)-(4*a*c))**(1/2)))/(2*a)
    print(f'root 1 is {root1}')
    print(f'root 2 is {root2}')
