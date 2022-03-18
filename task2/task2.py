from sys import argv


x = argv[1]
y = argv[2]

list1 = []
list2 = []


# получаем координаты точки и радиуса

with open(x) as file1:
    for line in file1:
        list1.append(list(map(float, line.strip('\n'))))


# получаем координаты точек
with open(y) as file2:
    for line in file2:
        list2.append(list(map(float, line.strip('\n'))))

x = list1[0][0]
y = list1[0][1]
r = list1[1][0]

for i in range(len(list2)):
    x_p = list2[i][0]
    y_p = list2[i][1]
    if len(list2) > 100:
        print(f'Количество точек {len(list2)}, максимальное число точек: 100')
        break
    else:
        if x_p == x or y_p == y:
            print(int(0))
        if (x - x_p)**2 / r**2 + (y - y_p)**2 / r**2 < 1:
            print(int(1))
        else:
            print(int(2))

















