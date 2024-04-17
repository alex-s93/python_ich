phrase = input('Enter a phrase: ').lower()

latin_alphabet = "abcdefghijklmnopqrstuvwxyz"

index = 0
is_pangram = True

while index < len(latin_alphabet):
    if latin_alphabet[index] not in phrase:
        is_pangram = False
        break
    index += 1

print("The phrase is", "" if is_pangram else "not", "a pangram")
