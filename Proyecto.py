# Proyecto Tienda de Mascotas Entregable
# Sanet Correa Castaño, Jhairo Esteban Muñeton Cortes
# 2025-2

class TiendaMascotas:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.__clientes = []         
        self.__mascotas = []
        self.__productos = []

    def getProductos(self):
        return self.__productos

    def getMascotas(self):
        return self.__mascotas

    def getClientes(self):
        return self.__clientes

    def AgregarCliente(self, cliente):
        self.__clientes.append(cliente) 

    def AgregarProducto(self, producto):
        self.__productos.append(producto)

    def AgregarMascota(self, mascota):
        self.__mascotas.append(mascota)

    def VenderProducto(self, usuario, idProducto):
        for producto in self.__productos:
            if producto.id == idProducto:
                usuario.productosComprados.append(producto)
                print(f"{usuario.nombre} compró {producto.nombre} por ${producto.precio}")
                return
        print("Producto no encontrado en la tienda")

    def VenderProducto(self, usuario, idProducto):
        for producto in self.__mascotas:
            if producto.id == idProducto:
                usuario.productosComprados.append(producto)
                print(f"{usuario.nombre} compró {producto.nombre} por ${producto.precio}")
                self.__mascotas.remove(producto)
                return
        print("Producto no encontrado en la tienda")

    def VenderMascota(self, usuario, idMascota):
        for mascota in self.__mascotas:
            if mascota.id == idMascota:
                usuario.mascotasCompradas.append(mascota)
                print(f"{usuario.nombre} compró {mascota.nombre} por ${mascota.precio}")
                return
        print("Mascota no encontrada en la tienda")

    def MostrarHistorialVentas(self):
        for cliente in self.__clientes:
            cliente.MostrarCompras()
    
    def MostrarProductos(self):
        for producto in self.__productos:
            producto.MostrarInfo()
                    
class Mascotas: 
    def __init__(self,idMascota, nombre, edad, especie):
        self.idMascota = idMascota
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def HacerSonido(self):
        pass

    def Comer(self):
        print(f"{self.nombre} está comiendo ")
    
    def MostrarAnimal(self):
        print(f"ID: {self.idMascota}, Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

class Perros(Mascotas):

    def HacerSonido(self):
        print(f"{self.nombre} hace guau guau")

class Gatos(Mascotas):
    def HacerSonido(self):
        print(f"{self.nombre} hace miau miau")

class Pez(Mascotas):
    def HacerSonido(self):
        print(f"{self.nombre} hace glu glu")

class Pajaro(Mascotas):
    def HacerSonido(self):
        print(f"{self.nombre} hace pio pio")

class Productos:
    def __init__(self, id, nombre, precio, tipo):
        self.id = id 
        self.nombre = nombre 
        self.precio = precio
        self.tipo = tipo
        
    def MostrarInfo(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio}, Tipo: {self.tipo}")

class Usuarios:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productosComprados = []
    

    def MostrarCompras(self):
        if not self.productosComprados:
            print(f"{self.nombre} no ha comprado nada todavía.")
        else:
            print(f"{self.nombre} ha comprado:")
            for producto in self.productosComprados:
                print(f"- {producto.nombre} (${producto.precio})")


tienda  = TiendaMascotas("C++cotas","Calle 123")           
print("Bienvenido a nuestra tienda")
print(tienda.nombre, "Direccion: ", tienda.direccion)
contador=0
while True:
    print("seleccione la opcion deseada")
    print("1. Agregar mercancia")
    print("2. Agregar mascota")
    print("3. Mostrar Productos")
    print("4. Mostrar Mascotas")
    print("5. Vender Producto")
    print("6. Vender Mascota")
    print("7. Mostrar Historial de ventas")
    print("0. Salir")

    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        nombre = input("ingresa El nombre del producto: ").capitalize()
        for producto in tienda.getProductos():
            if producto.nombre == nombre:
                print("El producto ya existe en la tienda")
                break
        contador += 1
        id = contador
        precio = float(input("ingresa el precio del producto: "))
        tipo = input("ingresa el tipo de producto (Alimento, Juguete, Accesorio)").capitalize()
        producto = Productos(id, nombre, precio, tipo)
        tienda.AgregarProducto(producto)
        print("Se ha añadido el producto exitosamente")
    elif opcion == 2:
        nomMascota = input("Ingrese el nombre de la mascota: ").capitalize()
        especieMascota = input("Ingrese la especie de la mascota (Perro, Gato, Pez): ").capitalize()
        edadMascota = int(input("Ingrese la edad de la mascota: "))
        contador += 1
        idMascota = contador
        for mascota in tienda.getMascotas():
            if mascota.nombre == nomMascota and mascota.especie == especieMascota:
                print("La mascota ya existe en la tienda")
                break
        if especieMascota == "Perro":
            mascota = Perros(idMascota, nomMascota, edadMascota, especieMascota)
            tienda.AgregarMascota(mascota)
        elif especieMascota == "Gato":
            mascota = Gatos(idMascota, nomMascota, edadMascota, especieMascota)
            tienda.AgregarMascota(mascota)
        elif especieMascota == "Pez":
            mascota = Pez(idMascota, nomMascota, edadMascota, especieMascota)
            tienda.AgregarMascota(mascota)
        elif especieMascota == "Pajaro":
            mascota = Pajaro(idMascota, nomMascota, edadMascota, especieMascota)
            tienda.AgregarMascota(mascota)
        else:
            print("especie no valida")
            
    elif opcion == 3:
        if not tienda.getProductos():
            print("No hay productos en la tienda")
        else:
            print("Productos disponibles en la tienda:")
            tienda.MostrarProductos() 

    elif opcion == 4:
        if not tienda.getMascotas():
            print("No hay mascotas en la tienda")
        else:
            print("Mascotas disponibles en la tienda:")
            for mascota in tienda.getMascotas():
                mascota.MostrarAnimal()
            
    elif opcion == 5:
        nombre = input("Ingrese su nombre: ").capitalize()
        existe = False
        usuario = None
        for i in tienda.getClientes():
            if i.nombre == nombre:        
                print("El cliente ya existe en la tienda, proceda con su compra")
                usuario = i
                existe = True
        
        if existe== False:
            usuario = Usuarios(nombre)
            tienda.AgregarCliente(usuario)
            print("Se ha añadido el cliente exitosamente")

        if not tienda.getProductos():
            print("No hay productos en la tienda")
        else:
            print("Productos disponibles en la tienda:")
            tienda.MostrarProductos() 
            idProducto = int(input("Ingrese el ID del producto que desea comprar: "))
            existe1 = False
            for producto in tienda.getProductos():
                if producto.id == idProducto:
                    tienda.VenderProducto(usuario, idProducto)
                    existe1 = True
                    break
            if existe1 == False:
                print("El producto no se encuentra en la tienda")

    elif opcion == 6:
        tienda.MostrarHistorialVentas() 

    elif opcion == 0:
        print("Gracias por visitar nuestra tienda")
        break
    
    else:
        print("Opcion no valida")