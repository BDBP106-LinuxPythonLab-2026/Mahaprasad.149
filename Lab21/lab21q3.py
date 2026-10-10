#Write a program to convert a tuple of angles into a list of tuples with each tuple containing
#the sine and cosine of an angle.

import math

angles = (30, 45, 60, 90)

result = list(map(lambda x: (math.sin(math.radians(x)), math.cos(math.radians(x))), angles))

print(result)

