from dataclasses import dataclass,field
from typing import List
import uuid

@dataclass
class Productos:
    id_producto: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    nombre: str
    precio: float
    tipo: str  
    def MostrarInfo(self) -> None: 
        print(f"ID: {self.id_producto}, Nombre: {self.nombre}, Precio: ${self.precio:,.2f}, Tipo: {self.tipo}")
    
    def GetId(self) -> str: 
        return self.id_producto

    def toFormatoCsv(self) -> List[str]:
        return [self.id_producto, self.nombre, str(self.precio), self.tipo]
