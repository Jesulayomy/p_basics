def time_stamp(n):
    print(f"Learning Python with mosh - {n}m")
    print('*' * 30)


def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("We will continue this course")


def calc_cost(total, shipping, discount):
    print(f"You are to pay: ${(total + shipping) - ((total + shipping) * discount)}")


def square_d(num):
    num *= num
    return num


time_stamp("2:30")
greet_user(last_name=input("Enter your first name: "), first_name=input("Enter you last name: "))

calc_cost(45, discount=0.1, shipping=5)

num2 = square_d(3)
print(num2)
