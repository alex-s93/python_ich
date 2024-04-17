# Напишите генератор, в который передаются строки разной длины и который
# возвращает строки фиксированной длины 7 символов. Если длина переданной
# строки больше 7 символов, то возвращаются первые 7 символов. Если длина
# переданной строки меньше 7 символов, то недостающие символы присоединяются
# к строке слева в виде нулей (“abcd” -> “000abcd”).
def generator(string):
    length = 7

    while True:
        if len(string) < length:
            string = "0"*(length - len(string)) + string
        elif len(string) > length:
            string = string[:length]

        string = yield string

gen = generator("test")
print(next(gen))

for i in ["test12345", "test123", "cat"]:
    print(gen.send(i))
