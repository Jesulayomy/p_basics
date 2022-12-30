class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Woof")


class Cat(Mammal):
    def meow(self):
        print("Meow")


def time_stamp(strn):
    print(f"Learning Python with mosh - {strn}m")
    print('*' * 30)


try:
    age = int(input('Age: '))
    income = int(input("Total life income: "))
    print(income / age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Age can't be 0
time_stamp("3:15")
