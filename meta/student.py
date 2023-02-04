from quirks import Quirk


class Student(Quirk):
    """ defines a student """

    def __init__(self, name="", grades={}):
        self.name = name
        self.grades = {'communication': 0, 'physical': 0, 'strategy': 0}

    def intro(self):
        print("My name is {} and I'm in class 1".format(self.name))
        print("Scores: \n\tComms {}\tPhysical {}\tStrat {}".format(self.grades['communication'], self.grades['physical'], self.grades['strategy']))

"""
    @property
    def grades(self):
        return self._name

    @grades.setter
    def grades(self, lst=[]):
        if len(lst) != 3:
            raise ValueError("Need a list of size 3")
        else:
            self.grades['communication'] = lst[0]
            self.grades['physical'] = lst[1]
            self.grades['strategy'] = lst[2]
"""
