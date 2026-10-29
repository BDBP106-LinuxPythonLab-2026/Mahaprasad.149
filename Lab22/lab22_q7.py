#Use the decorator measure_time to calculate how long the above function calculating population growth that loops 1 million iterations.
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
def population_growth():
    population = 1000

    for i in range(1_000_000):
        population += population * 0.001

    return population
final_population = population_growth()
print(f"Final population: {final_population:.2f}")
