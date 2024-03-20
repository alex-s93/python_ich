def number_length(number):
    length = 0
    while number != 0:
        length += 1
        number //= 10
    return length


origin_num = int(input("Enter an integer: "))

degree = number_length(origin_num) - 1
work_num = origin_num

index = 0
revers_num = 0

while index <= degree:
    digit = work_num % 10
    work_num //= 10
    revers_num += digit * 10 ** (degree - index)
    index += 1

print(origin_num, "is", "" if origin_num == revers_num else "not", "a palindrome")
