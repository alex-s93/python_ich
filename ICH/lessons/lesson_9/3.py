# Есть логическая переменная  weekday. Напишите программу, которая выводит сообщение
# “рабочий день”, если переменная истинна и сообщение  “выходной” - если ложна.

weekday = input("Enter a weekday(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ")

if weekday == "Saturday" or weekday == "Sunday":
    print("Today is day off")
else:
    print("Today is working day")
