def time_stamp(strn):
    print(f"Learning Python with mosh - {strn}m")
    print('*' * 30)


def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("We will continue this course")


def calc_cost(total, shipping, discount):
    print(f"You are to pay: ${(total + shipping) - ((total + shipping) * discount)}")


def square_d(num):
    num *= num
    return num


def convert_emoji(message):
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


time_stamp("2:30")
greet_user(last_name=input("Enter your first name: "), first_name=input("Enter you last name: "))

calc_cost(45, discount=0.1, shipping=5)

num2 = square_d(3)
print(num2)

custom_text = convert_emoji("Hello :), i am :| today :D")
print(custom_text)
