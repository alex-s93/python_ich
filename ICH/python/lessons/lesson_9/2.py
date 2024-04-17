# Дан прямоугольный треугольник с катетами 4 и 5 метра. Напишите программу,
# которая считает длину гипотенузы. Результат округлите до сотых.

cat_1 = int(input("Enter the length of the first cathetus:"))
cat_2 = int(input("Enter the length of the second cathetus:"))

hypotenuse = (cat_1**2 + cat_2**2) ** 0.5

print("The hypotenuse is:", round(hypotenuse, 2))