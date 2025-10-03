from abc import ABC, abstractmethod
from typing import List
from modelos import Cliente, LineaFactura

class Impuesto(ABC):
    @abstractmethod
    def calcular(self, cliente:Cliente, linea:LineaFactura)-> float:
        ...

class IVA(Impuesto):
    def calcular(self, cliente:Cliente, linea:LineaFactura)-> float:
        if linea.producto.categoria == "alimentos":
            return linea.subtotal * 0.0
        else:
            return linea.subtotal * 0.19
        
class Exento(Impuesto):
    def calcular(self, cliente:Cliente, linea:LineaFactura)-> float:
        return linea.subtotal * 0.08 if linea.producto.categoria != "servicios" else 0.0