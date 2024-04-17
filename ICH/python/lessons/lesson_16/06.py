# 6. Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переста-
# вьте эти слова местами. Результат запишите в строку и выведите получившуюся
# строку. При решении этой задачи не стоит пользоваться циклами и инструкцией if.

string = input("Enter two words separated by whitespace: ")

# new_string = string.split()[1] + " " + string.split()[0]
new_string = f"{string.split()[-1]} {string.split()[0]}"

print(new_string)
