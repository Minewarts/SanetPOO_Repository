'''class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def HacerSonido(self):
        pass

class Perro(Animal):
    def __init__(self,nombre,colorPelota)
        supper().__init__(nombre)
        self.colorPelota=colorPelota

    def HacerSonido(self):
        print(f'{self.nombre} Hace un wof wof')

class Gato(Animal):
    def HacerSonido(self):
        print(f'mi nombre es {self.nombre}, Comandante de los ejercitos del norte, General de las legiones Fenix y fiel sirviente del unico emperdor Marco Aurelio, Padre de un hijo asesinado, esposo de una esposa asesinada, y juro que me vengare, en esta vida o en la otra')


animal=Perro("Mia", "Rojo")
animal.HacerSonido()
animal2=Gato("Maximo Decimo Meridio")
animal2.HacerSonido()

print(isinstance(animal,Perro))
print(isinstance(animal2,Animal))
print(issubclass(Gato,Animal))
print(issubclass(Animal,Gato))'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def Respirar(self):
        print(f'{self.nombre} esta respirando')

class Estudiante(Persona):
    def __init__(self, nombre, edad, promedio):
        super().__init__(nombre, edad)
        self.promedio=promedio

    def Estudiar(self):
        print(f'{self.nombre} esta estudiando')



