#Write a decorator measure_time to calculate how long a function takes to run. Use it
#on a function that calculates the factorial of a number. Use a test case of calculating the
#factorial of 50.
import time
def measure_time(function):
    def wrapper(n):
        start=time.time()
        result=function(n)
        end=time.time()
        print("execution time:", end-start,"seconds")
        return result
    return wrapper
@measure_time
def factorial(n):
   fact=1
   for i in range(1,n+1):
       fact=fact*i
   return fact
factorial(50)
