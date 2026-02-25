import math
#1
x= int(input("input degree: "))
print(x/57.272893)
#2
x= int(input("height "))
y= int(input("Base, first value: "))
z= int(input("Base, second value: "))
jo=(y+z)/2 *x
print(f"Expected Output:  {jo}")
#3
n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

area = (n * a ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)
#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)