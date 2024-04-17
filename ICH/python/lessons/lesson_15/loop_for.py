letters = "ABCDefghKLM"

for i in letters:
    if i.upper() == i:
        letters = letters.replace(i, "")

print(letters)

#
# for i in letters:
#     if i.isupper():
#         letters = letters.replace(i, "")
#
# print(letters)
#
enumerate()