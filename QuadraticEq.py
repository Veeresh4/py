import cmath

a = int(input("enter the a value"))
b = int(input("enter the a value"))
c = int(input("enter the a value"))

d = (b**2)-(4*a*c)

x = (-b + cmath.sqrt(d))/(2*a)
y = (-b - cmath.sqrt(d))/(2*a)
print("solution of quadratic equ :", x,y)