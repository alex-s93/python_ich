def say_hi():
    global name
    name = "Tom"
    print("Hello", name)


name = "Alex"

say_hi()
print(name)


