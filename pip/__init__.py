import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

try:
    x = 13
    y = 0
    z = x / y
    print(z)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception ocurred")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
''' try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close() '''

x = 1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

p = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

username = str(input("Enter username: "))
print(f"Username is: {username}")

c = 12
txt = "I am {} years old"
print(txt.format(c))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

f = open("demo.txt", "rt")
z = open("tools.txt", "x")




























