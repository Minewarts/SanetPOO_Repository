from dataclasses import dataclass, field
from typing import List
from modelos import Cliente, LineaFactura, Producto
from impuesto import Impuesto
from descuentos import Descuento
@dataclass
class Factura:
    cliente: Cliente
    lineas: List[LineaFactura] = field(default_factory=list)

    def AgregarLinea(self, producto: Producto, cantidad = 1):
        self.lineas.append(LineaFactura(producto, cantidad))

    def CalcularDescuento(self, descuento:Descuento):
        return sum(descuento.aplicar(self.cliente,l) for l in self.lineas)
    
    def CalcularImpuesto(self, impuesto:Impuesto):
        return sum(impuesto.calcular(self.cliente,l) for l in self.lineas)
    
    def CalcularTotal(self, descuento:Descuento, impuesto:Impuesto):
        return sum(l.subtotal for l in self.lineas)+self.CalcularImpuesto(impuesto)-self.CalcularDescuento(descuento)
