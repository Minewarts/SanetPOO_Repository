'''class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.calificaciones=[]
    
    def MostrarDatos(self):
        print("Nombre: ",self.nombre,"Edad: ",self.edad,"Calificaciones: ",self.calificaciones)
    
    def CalcularPromedio(self):
        suma=sum(self.calificaciones)
        promedio=suma/len(self.calificaciones)
        return promedio
    
    def AñadirCalificacion(self,calificacion):
        self.calificaciones.append(calificacion) 


listaEstudiantes=[]
while True:
    print("-----//----- Menu -----//-----")
    print("1.Digitar nuevo estudiante y mostrar su promedio")
    print("2.Ver todos los registros")
    print("3.Salir")
    opcion=int(input("Ingrese su opcion: "))
    if opcion == 1:
        nombre=input("Ingrese su nombre: ")
        edad=int(input("Ingrese su edad: "))
        estudiante1= Estudiante(nombre,edad)

        for i in range (0,3):
            calificacion= float(input("Ingrese una nota: "))
            estudiante1.AñadirCalificacion(calificacion)
        promedio=estudiante1.CalcularPromedio()
        print (f'El promedio es: {promedio}')
        listaEstudiantes.append(estudiante1)
    
    elif opcion == 2:
        numeroEstudiantes = len(listaEstudiantes)
        print("El número de estudiantes es:", numeroEstudiantes)
        for estudiante in listaEstudiantes:
            estudiante.MostrarDatos()
    elif opcion == 3:
        break
    else:
        print("Opcion no valida")'''

#____________//___________//____________//___________//____________//___________//

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidadVendida):
        if cantidadVendida <= self.cantidad:
            self.cantidad -= cantidadVendida
            total = self.precio * cantidadVendida
            print(f"Se vendieron {cantidadVendida} unidades de '{self.nombre}'. Total: ${total}")
            print(f"Quedan {self.cantidad} unidades disponibles.")
        else:
            print(f"No hay suficientes unidades de '{self.nombre}'. Solo quedan {self.cantidad} unidades.")

    def mostrarInformacion(self):
        print(f"Código: {self.codigo}")
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad disponible: {self.cantidad} unidades")


def buscarProductoPorCodigo(codigoBuscado):
    for producto in listaDeProductos:
        if producto.codigo.lower() == codigoBuscado.lower():
            return producto
    return None

listaDeProductos = []

while True:
    print("_______// Menú //_______")
    print("1. Vender producto")
    print("2. Mostrar productos en stock")
    print("3. Salir")

    seleccion = input("Ingrese su selección: ")

    if seleccion == "1":
        codigo = input("Ingrese el código del producto: ")
        productoExistente = buscarProductoPorCodigo(codigo)

        if productoExistente:
            cantidadVender = int(input("Ingrese la cantidad que desea vender: "))
            productoExistente.vender(cantidadVender)
        else:
            print("Quiere Añadir Un producto?: ")
            seleccion2=str(input("Ingrese su opcion: "))

            if seleccion2.lower =="si":
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad disponible: "))
                nuevoProducto = Producto(codigo, nombre, precio, cantidad)
                listaDeProductos.append(nuevoProducto)
                nuevoProducto.mostrarInformacion()
                cantidadVender = int(input("Ingrese la cantidad que desea vender: "))
                nuevoProducto.vender(cantidadVender)
            else:
                print("El Producto no existe")

    elif seleccion == "2":
        if not listaDeProductos:
            print("No hay productos registrados.")
        else:
            print("\nProductos registrados:")
            for producto in listaDeProductos:
                producto.mostrarInformacion()

    elif seleccion == "3":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.")

#____________//___________//____________//___________//____________//___________//

'''class CuentaBancaria:
    def __init__(self, numeroCuenta, nombreTitular, saldoInicial):
        self.numeroCuenta = numeroCuenta
        self.nombreTitular = nombreTitular
        self.saldo = saldoInicial

    def depositarDinero(self, monto):
        self.saldo += monto
        print("Depósito exitoso. Nuevo saldo: $" + str(self.saldo))

    def retirarDinero(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro exitoso. Nuevo saldo: $" + str(self.saldo))
        else:
            print("Fondos insuficientes.")

    def consultarSaldo(self):
        print("Saldo actual: $" + str(self.saldo))


numeroCuenta = input("Ingrese el número de cuenta: ")
nombreTitular = input("Ingrese el nombre del titular: ")
saldoInicial = float(input("Ingrese el saldo inicial: "))

cuenta = CuentaBancaria(numeroCuenta, nombreTitular, saldoInicial)

while True:
    print("\1. Consultar saldo\n2. Depositar dinero\n3. Retirar Dinero\n4. Salir")


    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cuenta.consultarSaldo()
    elif opcion == "2":
        monto = float(input("Ingrese el monto a depositar: "))
        cuenta.depositarDinero(monto)
    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta.retirarDinero(monto)
    elif opcion == "4":
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida.")'''