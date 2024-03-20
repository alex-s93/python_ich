num_n = int(input("Enter a number N: "))

res = ""

current_num = 0
next_num = 1
iteration = 0

while iteration < num_n:
    if current_num == 0:
        res += str(current_num)
        current_num = 1
        iteration += 1
        continue

    res += "," + str(current_num)
    temp = current_num + next_num
    current_num = next_num
    next_num = temp
    iteration += 1

print(f"First {num_n} Fibonacci's number(s):", res)
