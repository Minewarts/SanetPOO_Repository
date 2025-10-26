from dataclasses import dataclass,field
from typing import List
from Mascotas import Mascotas
from Productos import Productos

@dataclass
class Usuarios:
    nombre: str
    __productosComprados: List[Productos]=field(repr=False,default_factory=list)
    __mascotasCompradas: List[Mascotas]=field(repr=False,default_factory=list)

    def AgregarProducto(self, producto: Productos) -> None:
        self.__productosComprados.append(producto)

    def AgregarMascota(self, mascota: Mascotas) -> None:
        self.__mascotasCompradas.append(mascota)

    def MostrarCompras(self):
        if not self.__productosComprados:
            print(f"{self.nombre} no ha comprado nada todavía.")
        else:
            print(f"{self.nombre} ha comprado:")
            for producto in self.__productosComprados:
                print(f"- {producto.nombre} (${producto.precio})")
    
    def MostrarMascotas(self):
        if not self.__mascotasCompradas:
            print(f"{self.nombre} no ha comprado mascotas todavía.")
        else:
            print(f"{self.nombre} ha comprado las siguientes mascotas:")
            for mascota in self.__mascotasCompradas:
                print(f"- {mascota.nombre} ({mascota.especie})")
                
    @property
    def GetListaProductos(self)-> List[Productos]:
        return self.__productosComprados
    
    @property
    def GetListaMascotas(self)-> List[Mascotas]:
        return self.__mascotasCompradas