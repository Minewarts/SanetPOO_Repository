from dataclasses import dataclass,field
from abc import abstractmethod,ABC
import uuid
from Excepciones import EdadInvalidaError
import random


@dataclass               
class Mascotas(ABC): 
    
    __idMascota: str = field(repr=False, init=False, default_factory=lambda: str(uuid.uuid4()))
    nombre: str
    edad: int
    precio: float
    
    def __post_init__(self):

        if self.edad < 0:
            raise EdadInvalidaError(self.edad)
    @abstractmethod
    def HacerSonido(self)->None:
        ...

    def Comer(self)-> str:
        print(f"{self.nombre} está comiendo ")
    
    def MostrarAnimal(self)-> str:
 
        print(f"ID: {self.__idMascota}, Especie: {type(self).__name__}, Nombre: {self.nombre}, Edad: {self.edad}, Precio: ${self.precio:,.2f}")

    def getId(self)-> str: 
        return self.__idMascota
    
    

class Perros(Mascotas):
    def HacerSonido(self)->str:
        print(f"{self.nombre} hace guau guau")

class Gatos(Mascotas):
    def HacerSonido(self)->str:
        print(f"{self.nombre} hace miau miau")

class Pez(Mascotas):
    def HacerSonido(self)->str:
        print(f"{self.nombre} hace glu glu")

class Pajaro(Mascotas):
    def HacerSonido(self)->str:
        print(f"{self.nombre} hace pio pio")