class Person:
    def __init__(self, first_name, last_name, year_of_birth, gender, alcohol_level):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.year_of_birth = int(year_of_birth)
        self.gender = str(gender)
        self.gender = alcohol_level

    @property
    def fullname(self):
        return self.first_name + " " self.last_name
