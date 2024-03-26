def sum_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_digits(num // 10)


number = int(input("Enter a number: "))
print(f"The sum of digits in number {number} is {sum_digits(abs(number))}")
