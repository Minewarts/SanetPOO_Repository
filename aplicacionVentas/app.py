from modelos import Cliente, Producto
from pedido import Factura
from impuesto import IVA, Exento
from descuentos import SinDescuento, DescuentoVIP, DescuentoVolumen

Cliente1 = Cliente(1, "Juan Perez", True)

Producto1 = Producto(1001, "Manzanas", "alimentos", 500.0)
Producto2 = Producto(1002, "Televisor", "electronica", 1500000.0)
Producto3 = Producto(1003, "Servicio de Limpieza", "servicios", 80000.0)
Producto4 = Producto(1004, "Arroz", "alimentos", 3000.0)
Producto5 = Producto(1005, "Celular", "electronica", 800000.0)

Factura1 = Factura(Cliente1)
Factura1.AgregarLinea(Producto1, 10)

descuentoAplicar= DescuentoVolumen()
impuestoAplicar=IVA()

print(Factura1.CalcularTotal(descuentoAplicar,impuestoAplicar))