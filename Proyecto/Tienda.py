from dataclasses import dataclass, field
from typing import List, Any
from Excepciones import ItemNoEncontradoError
from Usuarios import Usuarios
from Productos import Productos
from Mascotas import Perros, Gatos, Pez, Pajaro

@dataclass
class TiendaMascotas:
    nombre: str
    direccion: str
    __clientes: List[Usuarios]=field(repr=False,default_factory=list)
    __mascotas: list=field(repr=False,default_factory=list)
    __productos: list=field(repr=False,default_factory=list)

    def ActualizarBasesDatos(self):
        try:
            with open("productos.txt", "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(f"{p.id_producto},{p.nombre},{p.precio},{p.tipo}\n")

            with open("mascotas.txt", "w", encoding="utf-8") as f:
                for m in self.__mascotas:
                    f.write(f"{m.getId()},{m.nombre},{m.edad},{m.precio},{m.especie}\n")

            with open("usuarios.txt", "w", encoding="utf-8") as f:
                for u in self.__clientes:
                    productos_ids = ";".join([p.getId() for p in u.GetListaProductos])
                    mascotas_ids = ";".join([m.getId() for m in u.GetListaMascotas])
                    f.write(f"{u.nombre}|{productos_ids}|{mascotas_ids}\n")

            print("Datos guardados correctamente.")

        except Exception as e:
            print(f"Error al guardar datos: {e}")
            
def CargarDatos(self):
    try:
        self.__productos.clear()
        self.__mascotas.clear()
        self.__clientes.clear()

        # Cargar productos
        try:
            with open("productos.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    id_p, nombre, precio, tipo = linea.strip().split(",")
                    prod = Productos(nombre, float(precio), tipo)
                    prod._Productos__id_producto = id_p 
                    self.__productos.append(prod)
        except FileNotFoundError:
            pass

        try:
            with open("mascotas.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    id_m, nombre, edad, precio, especie = linea.strip().split(",")
                    edad = int(edad)
                    precio = float(precio)

                    if especie.lower() == "perro":
                        mascota = Perros(nombre, edad, precio)
                    elif especie.lower() == "gato":
                        mascota = Gatos(nombre, edad, precio)
                    elif especie.lower() == "pez":
                        mascota = Pez(nombre, edad, precio)
                    elif especie.lower() == "pajaro":
                        mascota = Pajaro(nombre, edad, precio)
                    else:
                        continue

                    mascota._Mascotas__id_mascota = id_m
                    self.__mascotas.append(mascota)
        except FileNotFoundError:
            pass

        # Cargar usuarios
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    nombre, productos_ids, mascotas_ids = linea.strip().split("|")
                    usuario = Usuarios(nombre)

                    # Vincular productos comprados
                    for pid in productos_ids.split(";"):
                        for p in self.__productos:
                            if p.getId() == pid:
                                usuario.AgregarProducto(p)

                    # Vincular mascotas compradas
                    for mid in mascotas_ids.split(";"):
                        for m in self.__mascotas:
                            if m.getId() == mid:
                                usuario.AgregarMascota(m)

                    self.__clientes.append(usuario)
        except FileNotFoundError:
            pass

        print("Datos cargados correctamente.")

    except Exception as e:
        print(f"Error al cargar datos: {e}")

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


    def VenderProducto(self, usuario: Usuarios, idProducto: str): 

        
        producto_a_vender = None
        for producto in self.__productos:

            if producto.GetId() == idProducto: 
                producto_a_vender = producto
                break
        
        if producto_a_vender:

            usuario.AgregarProducto(producto_a_vender) 
            print(f"¡Venta exitosa! {usuario.nombre} compró {producto_a_vender.nombre} por ${producto_a_vender.precio:,.2f}.")
        else:

            raise ItemNoEncontradoError(idProducto, "producto")


    def VenderMascota(self, usuario: Usuarios, idMascota: str): 

        
        mascota_a_vender = None
        for mascota in self.__mascotas:

            if mascota.getId() == idMascota:
                mascota_a_vender = mascota
                break
        
        if mascota_a_vender:

            usuario.AgregarMascota(mascota_a_vender)
            print(f"¡Venta exitosa! {usuario.nombre} compró {mascota_a_vender.nombre} por ${mascota_a_vender.precio:,.2f}.")
            self.__mascotas.remove(mascota_a_vender)
        else:

            raise ItemNoEncontradoError(idMascota, "mascota")

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