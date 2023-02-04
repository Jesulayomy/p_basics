class Laptop:
    """ Defines a laptop class used to store basic information """

    status = False

    def __init__(self, model):
        self.model = model

    def switch(self):
        """ Switches on or off the laptop """
        if Laptop.status == False:
            print("Switching on the device")
            Laptop.status = True
        else:
            print("Switching off the device")
            Laptop.status = False

    def cmd(self, command):
        """ Runs a command """
        print("You ran the command {}".format(command))


