print('Введите координаты первого угла')
x1 = int(input())
y1 = int(input())
print('Введите координаты второго угла')
x2 = int(input())
y2 = int(input())
a = abs(x1 - x2)
b = abs(y1 - y2)
s = (a * b)
p = (a + b) * 2
print("%.2f" % s)
print("%.2f" % p)