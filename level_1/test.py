from sys import stderr

stderr.write("Hello\n")

position = (11, 0)

if position[1] is not int and position[1] != 0:
    print("err")
