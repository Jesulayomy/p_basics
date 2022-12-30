import modules

modules.time_stamp("1:41")

numbers = [2, 7, 1, 3, 5, 7, 8, 9, 3, 7, 2, 5, 4, 6, 2]
names = ['John', 'Bon', 'Mosh', 'Sarah', 'Mary']
print(names[1])

n = numbers[0]
for num in numbers:
    if n < num:
        n = num
print(f"The largest number is: {n}")

numbers.append(20)
numbers.insert(0, 3)
numbers.remove(2)
# numbers.pop()
# print(numbers.index(3))
# print(numbers.count(2))
print(11 in numbers)
print(numbers)
numbers.sort()
print(numbers)

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

modules.time_stamp("2:10")

numbers2 = (7, 1, 3, 5, 7, 8, 9, 3, 7, 2)
# numbers2[2] = 13

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
a = x * y * z

b = coordinates[0] * coordinates[1] * coordinates[2]

c, d, e = coordinates
f = c * d * e

print(a, b, f)

modules.time_stamp("2:27")
message = input("> ")
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

print(words)
print(output)
