import math

print("Enter coefficient for the definition.")
print("ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4 * a * c
print("Discriminant is: " + str(d))

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(round(x1, 2), round(x2, 2))
elif d == 0:
    x = -b / (2 * a)
    print(round(x, 2))
else:
    print("There are no roots.")