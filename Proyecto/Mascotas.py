from dataclasses import dataclass,field
from abc import abstractmethod,ABC
import uuid


@dataclass               
class Mascotas(ABC): 
    
    __idMascota: str = field(repr=False, init=False, default_factory=lambda: str(uuid.uuid4()))
    nombre: str
    edad: int
    especie: str
    @abstractmethod
    def HacerSonido(self)->None:
        ...

    def Comer(self)-> str:
        print(f"{self.nombre} está comiendo ")
    
    def MostrarAnimal(self)-> str:
        print(f"ID: {self.idMascota}, Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

    def getId(self)-> int:
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