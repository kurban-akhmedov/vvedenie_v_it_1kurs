def(x, y, z):
    

banana = 2.50
apple = 1.20
orange = 0.85
grapefruit = 1.45
kiwi = 2.70
pineapple = 5.50
grapes = 3.85



banana_1 = 2.70
apple_1 = 1.25
orange_1 = 0.90
grapefruit_1 = 1.60
kiwi_1 = 3.00
pineapple_1 = 5.60
grapes_1 = 4.20
price = 0

print('Введите фрукт')
string = input()
print('Введите день недели')
day = input()
print('Введите массу')
weight = float(input())

for budni in banana, apple, orange, grapefruit, kiwi, pineapple, grapes:
    if day != 'Saturday' and day != 'Sunday':
        price = string *