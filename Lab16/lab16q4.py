""""Take input angle in degrees convert the to radian and find all six trignometric values"""

import math


from PIL.GimpGradientFile import sine

angle = float(input("Enter angle in degrees: "))
radian = angle*math.pi/180

sin=float(math.sin(radian))
cos=float(math.cos(radian))
tan=float(math.tan(radian))
cot=float(1/math.tan(radian))
sec=float(1/math.cos(radian))
cosec=float(1/math.sin(radian))

print("sin" + (str(angle)) + "=" + str(sin))
print("cos" + (str(angle)) + "=" + str(cos))
print("tan" + (str(angle)) + "=" + str(tan))
print("cot" + (str(angle)) + "=" + str(cot))
print("sec" + (str(angle)) + "=" + str(sec))
print("cosec" + (str(angle)) + "=" + str(cosec))

