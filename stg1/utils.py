import random


def sent_to_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":|": "😐",
        ":D": "😀",
        ":(": "🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


def find_max(numbers):
    max_num = numbers[0]
    for element in numbers:
        if element > max_num:
            max_num = element
    return max_num


def time_stamp(strn):
    print(f"Learning Python with mosh - {strn}m")
    print('*' * 30)


def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("We will continue this course")


def calc_cost(total, shipping, discount):
    print(f"You are to pay: ${(total + shipping) - ((total + shipping) * discount)}")


def square_d(num):
    return num * num


class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Woof")


class Cat(Mammal):
    def meow(self):
        print("Meow")


class Person:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        print(f"{self.name}: {self.message}")

    def talk(self, message):
        self.message = message
        print(f"{self.name}: {self.message}")


def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f"({d1}, {d2})")
