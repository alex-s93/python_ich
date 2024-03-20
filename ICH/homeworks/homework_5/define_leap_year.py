year = int(input("Введите год: "))

# First option for solving the task
is_leap_year = False

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap_year = True

print("Год високосный? -", is_leap_year)

# Second option for solving the task
is_leap = "не "

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap = ""

print(f"Год {is_leap}является високосным.")
