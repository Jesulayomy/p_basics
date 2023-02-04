from pc import Laptop
class Human(Laptop):
    """ Human being vlass """

    status = True

    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def sleep(self):
        if Human.status == True:
            print("Making the bed...")
            print("{} is now sleeping".format(self.name))
        else:
            print("{} is already asleep".format(self.name))
        Human.status = False

    def wake(self):
        if Human.status == False:
            print("Waking up...")
            print("{} is now awake".format(self.name))
        else:
            print("I'm already awake")
        Human.status = True
