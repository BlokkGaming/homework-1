print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x = int(input('введите x (0/1):'))
y = int(input('введите y (0/1):'))
z = int(input('введите z (0/1):'))

if x == 1 or y == 1 or z == 1:
    res1 = 0
else:
    res1 = 1

if x == 1 and y == 1 and z == 1:
    res2 = 1
else:
    res2 = 0 
print(str(res1) + ', ' + str(res2))