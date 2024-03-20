# 3. Для данной строки, напечатать строку, где каждый символ повторяется
# дважды. Например, 'The' → 'TThhee', 'AAbb' → 'AAAAbbbb'.
string = input("Enter something: ")

# new_string = ""
#
# for i in string:
#     new_string += i * 2
#
# print(new_string)

for i in string:
    print(i*2, end='')
print()
