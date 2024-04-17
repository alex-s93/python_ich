year = int(input("Enter a year: "))

if year <= 1965:
    generation = "Baby boom"
elif year <= 1980:
    generation = "generation x"
elif year <= 1996:
    generation = "generation y"
else:
    generation = "generation z"

print("the generation is ", generation)

