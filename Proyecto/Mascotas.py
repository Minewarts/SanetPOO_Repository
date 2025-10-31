from dataclasses import dataclass,field
from abc import abstractmethod,ABC
import uuid
from Excepciones import EdadInvalidaError
import random

def generar_mascota_id():
    return "M" + str(random.randint(1, 99999)).zfill(5)

class Mascotas(ABC):  
    def __init__(self, nombre: str, edad: int, precio: float):
        if edad < 0:
            raise EdadInvalidaError(edad)
        self.nombre = nombre
        self.edad = edad
        self.precio = precio
        self.__id_mascota = generar_mascota_id()
        self.especie = type(self).__name__

    def MostrarInfo(self) -> None:
        print(f"ID: {self.__id_mascota}, Nombre: {self.nombre}, Edad: {self.edad}, Precio: ${self.precio:,.2f}, Especie: {self.especie}")

    def getId(self):
        return self.__id_mascota
    
    @abstractmethod
    def HacerSonido(self):
        ...



@dataclass
class Perros(Mascotas):
    def __init__(self, nombre: str, edad: int, precio: float):
        super().__init__(nombre, edad, precio)
        self.especie = "Perro"
    def HacerSonido(self):
        print(f"{self.nombre} hace guau guau", end="")

@dataclass
class Gatos(Mascotas):
    def __init__(self, nombre: str, edad: int, precio: float):
        super().__init__(nombre, edad, precio)
        self.especie = "Gato"
    def HacerSonido(self):
        print(f"{self.nombre} hace miau miau", end="")

@dataclass
class Pez(Mascotas):
    def __init__(self, nombre: str, edad: int, precio: float):
        super().__init__(nombre, edad, precio)
        self.especie = "Pez"
    def HacerSonido(self):
        print(f"{self.nombre} hace glu glu", end="")

@dataclass
class Pajaro(Mascotas):
    def __init__(self, nombre: str, edad: int, precio: float):
        super().__init__(nombre, edad, precio)
        self.especie = "Pajaro"
    def HacerSonido(self):
        print(f"{self.nombre} hace pio pio", end="")