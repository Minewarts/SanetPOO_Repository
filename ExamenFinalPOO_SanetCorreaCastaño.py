from abc import ABC
from dataclasses import dataclass
@dataclass
class Item: 
    precio:float
    nombre:str

@dataclass
class Cliente:
    __id_cliente:int
    nombre:str

class LineaPedido:
    def __init__(self, cantidad:int):
        self.cantidad=cantidad
        self.producto=None

    def set_producto(self,item):
        producto=item

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

class Pedido:
    def __init__(self):
        lineas=[]
        cliente=None
    def añadir_lineas(self,linea):
        self.lineas.append(linea)

    def asignar_cliente(self, cli):
        self.cliente=cli

    def calcularSubtotal(self):
        for i in self.lineas:
            suma+= i.calcular_subtotal()

class Envio(ABC):
    def __init__(self,costo_base,tipo, velocidad):
        self.costo_base=costo_base
        self.tipo=tipo
        self.velocidad=velocidad

    def calcular_costo(pedido):
        ... 



