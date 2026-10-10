""""Write a program to tell which quadrant a given point lies in the first, second , third or fourth quadrant """
X=int(input("Enter a number: "))
Y=int(input("Enter a number: "))

if X>0 & Y>0:
    print("Given point is in 1st quadrant")
elif X>0 & Y<0:
    print("Given point is in 4th quadrant")
elif X<0 & Y<0:
    print("Given point is in 3rd quadrant")
elif X<0 & Y>0:
    print("Given point is in 2nd quadrant")





