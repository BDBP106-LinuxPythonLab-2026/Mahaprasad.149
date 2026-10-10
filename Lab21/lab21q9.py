#Write a function population_growth(initial,rate, time) that defines an inner func-tion exponential_growth()
#using the formula N(t) = N0 + exp(rate ∗ time) where N0
#represents the initial population and N(t) is population after time t. The inner function
#returns the population after time, and the outer function rounds and prints it.

initial = float(input("Enter initial population: "))
rate = float(input("Enter growth rate: "))
time = float(input("Enter time: "))
import math

def population_growth(initial, rate, time):
    def exponential_growth():
        return initial + math.exp(rate * time)

    population = exponential_growth()
    print(round(population))

population_growth(initial, rate, time)