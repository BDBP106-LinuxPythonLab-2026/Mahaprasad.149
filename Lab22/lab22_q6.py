#Write a function population_growth(initial,rate, time) that defines an inner function exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0 represents the initial population and N(t) is population after time t. The inner function returns the population after time, and the outer function rounds and prints it (already done in Labmport math
import math
def population_growth(initial,rate,time):
    def exponential_growth():
        return initial*math.exp(rate*time)
    population=exponential_growth()
    print(round(population))
population_growth(1000,0.05,10)
print(population_growth)