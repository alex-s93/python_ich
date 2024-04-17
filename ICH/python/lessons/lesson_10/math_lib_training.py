import decimal

while True:
    number = input("Enter a natural number: ")
    if number.isdigit() and int(number) != 0:
        number = int(number)
        break
    print("You entered a non-natural number")

n = 0

result_1 = 0
decimal.getcontext().prec = 30
result_2 = decimal.Decimal('0')

while n < number:
    result_1 += ((-1) ** n) / (2 * n + 1)
    result_2 += decimal.Decimal.from_float(((-1) ** n) / (2 * n + 1))
    n += 1

print(f"The sum of the first {number} Leibniz's numbers is: ", result_1)
print(f"The sum of the first {number} Leibniz's numbers is: ", result_2)


# The sum of the first 1001 Leibniz's numbers is:  0.7856479135848861
# The sum of the first 10001 Leibniz's numbers is:  0.7854231608976336

# The sum of the first 1001 Leibniz's numbers is:  0.785647913584885803999456610480
# The sum of the first 10001 Leibniz's numbers is:  0.785423160897635844781812866621