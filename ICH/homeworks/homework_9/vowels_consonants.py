phrase = input('Enter a phrase: ').lower()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

index = 0
vowels_count = 0
consonants_count = 0

while index < len(phrase):
    if phrase[index] in vowels:
        vowels_count += 1

    if phrase[index] in consonants:
        consonants_count += 1

    index += 1

print('Number of vowels: ', vowels_count)
print('Number of consonants: ', consonants_count)
