num = int(input("Enter a natural decimal number:"))

res = ""
temp_num = num

while True:
    if temp_num == 1:
        res = str(temp_num) + res
        break

    res = str(temp_num % 2) + res
    temp_num = temp_num // 2
    continue

print("The binary view of number", num, "is", res)
