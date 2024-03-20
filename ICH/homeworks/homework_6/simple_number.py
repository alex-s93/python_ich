num = int(input("Enter a positive integer: "))

count = 1

is_simple = True

while num - count > 1:
    print(num - count)
    if num % (num - count) == 0:
        is_simple = False
        break

    count += 1

print("The number ", num, " is ", "" if is_simple else "not ", "simple", sep="")
