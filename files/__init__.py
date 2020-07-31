#f = open("file.txt", "r")
#print(f.read())
#print(f.readline())
#print(f.read())


#Agrega contenido an un txt

def add():
    f = open("file.txt", "a")
    f.write("Now the file has more content!\n")
    f = open("file.txt", "r")
    print(f.read())

#Sobrescribe el txt

def overwrite():
    p = open("filev2.txt", "w")
    p.write("Savanna\n")
    p = open("filev2.txt", "r")
    print(p.read())

def create():
    m = open("filev3.txt", "x")
    m.write("Read in line\n")
    m = open("filev3.txt", "r")
    print(m.read())

create()










































