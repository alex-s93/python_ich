def number_length(number):
    length = 0
    while number != 0:
        length += 1
        number //= 10
    return length


origin_num = int(input("Enter an integer: "))

degree = number_length(origin_num)
work_num = origin_num

index = 0
nums_sum = 0

while index < degree:
    digit = work_num % 10
    work_num //= 10
    nums_sum += digit ** degree
    index += 1

print(origin_num, "is", "" if origin_num == nums_sum else "not", "a Armstrong's number")
