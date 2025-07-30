#Definicion de clases
class Perro:
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
    
    def Ladrar(self):
        print(f'{self.nombre} esta ladrando')

class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo


#Instanciar Objetos

miPerrito1=Perro("Douglas", "Labrador")
miPerrito2=Perro("Canela", "Chanda")
miPerrito3=Perro(input("Ingrese el nombre del perro "),input("Ingrese la raza del perro "))

print (miPerrito1.raza,miPerrito1.nombre)
print (miPerrito2.raza,miPerrito2.nombre)
print (miPerrito3.raza,miPerrito3.nombre)

miPerrito3.Ladrar()