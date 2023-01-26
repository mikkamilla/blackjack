class Student:
    def __init__(self, name, surname, dob, country):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.country = country
    def greeting(self):
        print(f"Hello, my name is {self.name}")
        

class ForeignStudent(Student):
    def greeting(self):
        print("Ma io sono Giapponese")


# sample = Student("Manuel", "Mastrominico", "05/01/2005", "Ireland")
# sample.greeting()
# print(sample.name)
# sample2 = ForeignStudent("Michele", "Mastrominico", "05/01/2005", "Ireland")
# sample2.greeting()
# print(sample2.name)


deck =
    