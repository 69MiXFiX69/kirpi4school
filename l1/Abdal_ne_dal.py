import math

a = float(input("Enter triangle's side a: "))
b = float(input("Enter triangle's side b: "))
c = float(input("Enter triangle's side c: "))


def perimetr(a,b,c):
    p = (a + b + c) / 2
    h = ((2 / a) * math.sqrt(p * (p - a) * (p - b) * (p - c)))
    x = c*h/(c+h)
    return x

print(perimetr(a, b, c))