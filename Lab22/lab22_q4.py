#Write a decorator called check_positive that checks whether the argument passed to a function is positive. If it is positive, execute the function; otherwise, print "Number must be positive".
def check_positive(function):
    def wrapper(number):
        if number>0:
            function(number)
        else:
            print("Number must be positive")
    return wrapper
@check_positive
def display_number(number):
    print("Number is:",number)
display_number(5)
display_number(0)
display_number(-3)