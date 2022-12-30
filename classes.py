# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")
#
#
# point1 = Point(0, 3)
# point1.draw()
#
# print(point1.x, point1.y)
#
# point2 = Point(3, 7)
# point2.draw()

class Person:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        print(f"{self.name}: {self.message}")

    def talk(self, message):
        self.message = message
        print(f"{self.name}: {self.message}")


layo = Person("Jesulayomi", "Good morning")
layo.talk("Hello")
layo.talk("Hope you had a wonderful holiday")
