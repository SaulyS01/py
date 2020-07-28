class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Students(Person):
  def __init__(self, fname, lname, year):
    super().__init__(lname, fname)
    self.age = year

  def welcome(self):
    print(f"Welcome {self.firstname} {self.lastname} to the class of {self.age}")

x = Students("Saul", "Ytucayasi", 2003)
x.welcome()



