from random import randint

random_num = randint(1, 100)

while True:
    num = int(input("Guess the number between 1 and 100: "))

    if random_num == num:
        print("You guessed!")
        break

    if random_num > num:
        print("Your number is smaller than the hidden number. Try again.")
    else:
        print("Your number is bigger than the hidden number. Try again")
