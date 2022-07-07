point_1 = []
point_2 = []

point_1.append(int(input('Введите X первой точки - ')))
point_1.append(int(input('Введите Y первой точки - ')))
point_2.append(int(input('Введите X второй точки - ')))
point_2.append(int(input('Введите Y второй точки - ')))

distance = ((point_2[1] - point_1[1])**2 + (point_2[0] - point_1[0])**2)**0.5

print(round(distance, 2))
