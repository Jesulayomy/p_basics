print("Learning Python with mosh - 58m")
print('*' * 30)

is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Drink a cup of coffee")
else:
    print("It's a lovely day")
print("Have a nice day")

print("Learning Python with mosh - 1:04m")
print('*' * 30)

price = 1000000
good_credit = False
if good_credit:
    pay = price * 0.1
else:
    pay = price * 0.2

print(f"The house price is ${price}")
print(f'You are required to pay a deposit of: ${pay}')

print("Learning Python with mosh - 1:12m")
print('*' * 30)

temp = input('Enter the current temperature in Celsius: ')

if int(temp) > 30:
    print("It's a hot day")
elif int(temp) < 10:
    print("It's a cold day")
else:
    print("It's a lovely day")

name = input("Enter your name: ")
min_name_length = 3
max_name_length = 50

if len(name) < min_name_length:
    print(f"'{name}' is less than the minimum length of {min_name_length}")
elif len(name) > max_name_length:
    print(f"'{name}' is greater than the maximum length allowed ({max_name_length})")
else:
    print(f"'{name}' approved")
