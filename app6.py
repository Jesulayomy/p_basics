print("Learning Python with mosh - 2:20m")
print('*' * 30)

customer = {
    "name": "Cobol Abraham",
    "age": 30,
    "is_variable": True
}
customer["birth_date"] = "Jan 1 1980"
print(customer.get("name", "Jan 1 1980"))

phone_number = input("Phone: ")
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for number in phone_number:
    print(words[int(number)])

phone = input("Phone: ")
mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for char in phone:
    output += mapping.get(char, "!") + " "
print(output)
