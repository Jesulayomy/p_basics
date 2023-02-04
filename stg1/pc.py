class Laptop:
    """ Defines a laptop class used to store basic information """

    state = False

    def __init__(self, model):
        self.model = model + '2022'

    def switch(self):
        """ Switches on or off the laptop """
        if Laptop.state == False:
            print("Switching on the device")
            Laptop.state = True
        else:
            print("Switching off the device")
            Laptop.state = False

    def cmd(self, command):
        """ Runs a command """
        print("You ran the command: '{}'".format(command))


