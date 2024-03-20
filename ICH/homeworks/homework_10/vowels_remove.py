string = input("Enter a sentence to remove vowels: ")

vowels = "aeiou"
index = 0

while index < len(string):
    if string[index].lower() in vowels:
        string = string.replace(string[index], "")
        string = string.replace(string[index].lower(), "")
    index += 1

print("The modified string is:", string)