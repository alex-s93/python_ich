name = input("Enter your name: ")
balance = input("Balance: ")

greeting = "Hello, {name}! Your balance is {bal}. Bye {name}".format(name=name, bal=balance)

print(greeting)