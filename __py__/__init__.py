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

for x in [1, 2, 3, 4, 5]:
  print(f"La variable es {x} su cuadrado es {x**2}")

x = 20
print("Tabla de multiplicar advance")
for x in [1, 2, 3, 4, 5]:
  print(f"{x} x {x+1} = {x*(x+1)}")

for x in "FORM":
  print(f" La letra es: {x}")

times = int(input("Ingrese la cantidad de veces: "))
for x in range(times):
  print("Hello")

count = 0
for x in range(1, 6):
  if x % 2 == 0:
    count += 1
print(f"Se hallaron {count} multiplos de 2")

find = False
for x in range(1, 6):
  if x % 2 == 0:
    find = True
if find:
  print(f"Verdadero")
else:
  print(f"Falso")

x = 1
while x <= 5:
  print(x)
  x += 1









































