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

#modulos:

import module as x
x.greeting("Saul")

y = x.person["name"]
print(y)

#z = dir(x)
#print(z)

from module import person
print(person["age"])

import datetime
x = datetime.datetime.now()
print(x.year, x.strftime("%A"), x.strftime("%B"))

import math
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x, y)
x = abs(-7)
print(x)
x = pow(2, 6)
print(x)
x = math.sqrt(81)
print(x)

import json
x = '{"name":"Jhon", "age": 30, "city": "New York"}'
y = json.loads(x)
print(y["age"])
print()

#z = json.dumps(x)
#print(z)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("\n")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent = 4, sort_keys = True))

#Regex module

import re
txt = str(input("Ingrese la palabra: "))
u = re.search("^The.*Spain$", txt)
if u:
  print("Correcto amigo")
else:
  print("Incorrecto ingrese nuevamente")

import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))




































