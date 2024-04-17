# Сейчас на часах 9 часов 45 минут утра. Напишите программу, которая считает
# количество секунд, прошедшее с полуночи.

hours = int(input("Enter the hour:"))
minutes = int(input("Enter the minutes:"))

seconds_from_midnight = hours * 60 * 60 + minutes * 60

print("Amount of seconds since midnight:", seconds_from_midnight)
