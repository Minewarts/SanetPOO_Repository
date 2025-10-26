from dataclasses import dataclass,field
from typing import List, Any
from Excepciones import ItemNoEncontradoError 
from Usuarios import Usuarios

@dataclass
class TiendaMascotas:
    nombre: str
    direccion: str
    __clientes: List[Usuarios]=field(repr=False,default_factory=list)
    __mascotas: list=field(repr=False,default_factory=list)
    __productos: list=field(repr=False,default_factory=list)

    def ActualizarBasesDatos(self):

        print("Guardando datos de clientes en Clientes.csv...")
        try:
            with open ('Clientes.csv', 'w') as f:

                f.write('Nombre,Mascotas_Compradas_IDs,Productos_Comprados_IDs\n')
                for c in self.__clientes:

                    mascotas_nombres = ";".join([m.nombre for m in c.GetListaMascotas])
                    productos_nombres = ";".join([p.nombre for p in c.GetListaProductos])
                    
                    f.write(f'{c.nombre},"{mascotas_nombres}","{productos_nombres}"\n')
            print("Base de datos de clientes actualizada correctamente.")
        except Exception as e:
            print(f"Error al escribir en Clientes.csv: {e}")


    def getProductos(self) -> list:
        return self.__productos

    def getMascotas(self)-> list:
        return self.__mascotas

    def getClientes(self)-> list:
        return self.__clientes

    def AgregarCliente(self, cliente: Usuarios):
        self.__clientes.append(cliente) 

    def AgregarProducto(self, producto: Any):
        self.__productos.append(producto)

    def AgregarMascota(self, mascota: Any):
        self.__mascotas.append(mascota)


    def VenderProducto(self, usuario: Usuarios, idProducto: int):

        
        producto_a_vender = None
        for producto in self.__productos:
            if producto.id == idProducto:
                producto_a_vender = producto
                break
        
        if producto_a_vender:

            usuario.agregar_producto(producto_a_vender) 
            print(f"¡Venta exitosa! {usuario.nombre} compró {producto_a_vender.nombre} por ${producto_a_vender.precio}.")
        else:

            raise ItemNoEncontradoError(str(idProducto), "producto")

    def VenderMascota(self, usuario: Usuarios, idMascota: int):

        
        mascota_a_vender = None
        for mascota in self.__mascotas:
            if mascota.id == idMascota:
                mascota_a_vender = mascota
                break
        
        if mascota_a_vender:

            usuario.agregar_mascota(mascota_a_vender)
            print(f"¡Venta exitosa! {usuario.nombre} compró {mascota_a_vender.nombre} por ${mascota_a_vender.precio}.")
            self.__mascotas.remove(mascota_a_vender)
        else:

            raise ItemNoEncontradoError(str(idMascota), "mascota")

    def MostrarHistorialVentas(self):
        if not self.__clientes:
            print("No hay clientes registrados ni ventas en el historial.")
            return
            
        print("\n--- Historial de Ventas por Cliente ---")
        for cliente in self.__clientes:
            cliente.MostrarCompras()
            
    def MostrarProductos(self):
        if not self.__productos:
            print("El inventario de productos está vacío.")
            return
            
        print("\n--- Inventario de Productos ---")
        for producto in self.__productos:
            producto.MostrarInfo()