b = True
while b == True:
    a = input('день недели: \n')
    a = int(a)
    if a > 0 and a < 6:
        print('нет')
        b = False
    elif a == 6 or a == 7:
        print('да')
        b = False
    else:
        print('введите день недели цифрой от 1 до 7')
