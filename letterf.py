numbers = [2, 7, 2, 5]

for num in numbers:
    print('x' * num)

names = ['John', 'Bon', 'Mosh', 'Sarah', 'Mary']
print(names[1])
n = numbers[0]

for num in numbers:
    if n < num:
        n = num

print(f"The largest number is: {n}")
