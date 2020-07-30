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

#nonlocal = variables intermedias
#global = variables globales

mytuple = ("taxi", "toyota")
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))

mylist = ["hello", "world"]
for x in mylist:
  print(x, end = " ")
print("")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

def greeting(name):
  print("Hello, " + name)












































