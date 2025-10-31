from typing import List
import random

def generar_producto_id():
    return "P" + str(random.randint(1, 99999)).zfill(5)

class Productos:
    def __init__(self, nombre: str, precio: float = 0.0, tipo: str = ""):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__id_producto = generar_producto_id()
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    @property
    def id_producto(self) -> str:
        return self.__id_producto

    def getId(self) -> str:
        return self.__id_producto

    def GetId(self) -> str:
        return self.__id_producto

    def MostrarInfo(self) -> None:
        print(f"ID: {self.__id_producto}, Nombre: {self.nombre}, Precio: ${self.precio:,.2f}, Tipo: {self.tipo}")

    def toFormatoCsv(self) -> List[str]:
        return [self.__id_producto, self.nombre, str(self.precio), self.tipo]