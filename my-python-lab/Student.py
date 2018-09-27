class Student:
    ## define what a student is
    ## when class is called var passed values are being passed
    ## actual object are actually passed to their attributes
    ## self.name is an attribute of name and so on
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

