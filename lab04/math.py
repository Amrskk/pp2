import math
def dtr(degrees):
    return degrees * (math.pi / 180)

degrees = int(input("Input degree: "))
radians = dtr(degrees)
print(f"Output radian: {radians}")
