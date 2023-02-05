from quirks import Quirk


class Student(Quirk):
    """ defines a student """

    class_size = 0

    def __init__(self, name="Extras", grades=[0, 0, 0]):
        self.name = name
        self._comm = grades[0]
        self._phys = grades[1]
        self._stam = grades[2]
        Student.class_size += 1

    def intro(self):
        """ Introduces a student """
        print("My name is {} and I'm in class 1".format(self.name))
        print("Scores: \n    Comms: {}    Physical: {}    Strat: {}".format(self._comm, self._phys, self._stam))

    @property
    def comm(self):
        """ Communications returned """

        return self._comm

    @comm.setter
    def comm(self, upgrade):
        """ Increases the communication skill by upgrade amount """

        self._comm = upgrade
