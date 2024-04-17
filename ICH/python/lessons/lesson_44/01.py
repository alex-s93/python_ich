class MyClass:

    def general_method(self, a, b):

        print("general method", self.__class__.__name__)
        return a + b

    @classmethod
    def static_method(cls, a, b):
        print("static method")
        return a + b


if __name__ == "__main__":
    print(MyClass.static_method(1, 2))
