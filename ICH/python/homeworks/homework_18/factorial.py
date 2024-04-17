def factorial_loop(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


def factorial_recursion(num):
    if num == 1:
        return 1
    elif num > 1:
        return num * factorial_recursion(num - 1)


number = int(input("Enter a number for factorial calculation: "))

print(f"The factorial of number '{number}' is '{factorial_loop(number)}' (resolved by loop method)", )
print(f"The factorial of number '{number}' is '{factorial_recursion(number)}' (resolved by recursion)", )
