print("Learning Python with mosh - 1:12m")
print('*' * 30)

i = 9
guess = 0
guess_count = 0

while guess_count < 10:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == i:
        print("Correct Number")
        print(f"You made {guess_count} guesses")
        break
else:
    print(f"You could not guess correctly in {guess_count} tries")

print("Learning Python with mosh - 1:41m")
print('*' * 30)

for item in range(10, 100, 5):
    print(item)

cart_prices = [142, 41, 142, 64, 1236, 246, 143, 135, 246, 351]
total = 0

for item in cart_prices:
    print(f"Total + Item:    {total} + {item}")
    total += item

print(f"Total = {total}")
