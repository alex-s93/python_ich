num = int(input("Enter a number: "))

# if num == 0:
#     res = "is nil"
# elif num % 2 == 0:
#     res = "is even"
# else:
#     res = "is odd"

res = "is nil" if num == 0 else "is even" if num % 2 == 0 else "is odd"
print(num, res)
