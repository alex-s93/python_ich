x1, y1 = input("Введите координаты первой точки (x1, y1): ").split(",")
x2, y2 = input("Введите координаты второй точки (x2, y2): ").split(",")

distance = ((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5
print("Расстояние между точками: ", distance)
