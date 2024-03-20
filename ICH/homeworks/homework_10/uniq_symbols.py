string = input("Enter a sentence to check for uniq symbols:").lower()

index = 0
repeated_symbols = ""

while index < len(string):
    if string[index + 1:].find(string[index]) != -1:
        if string[index] not in repeated_symbols:
            repeated_symbols += f"`{string[index]}`,"
    index += 1
else:
    repeated_symbols = repeated_symbols.rstrip(",")

if repeated_symbols == "":
    print("The entered string is uniq")
else:
    print("The next symbols is repeated: ", repeated_symbols)