import math

ax = int(input('x первой точки: '))
ay = int(input('y первой точки: '))
bx = int(input('x второй точки: '))
by = int(input('y второй точки: '))

x = (ax - bx) ** 2
y = (ay - by) ** 2

s = math.sqrt(x + y)

print(s)
