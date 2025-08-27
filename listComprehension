'''lista=[[i and j for j in range(1, 11)] for i in range(1, 11)]
print(lista)'''


import random
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = []
        
    def agregarCuenta(self, cuenta):
        self.cuenta.append(cuenta)
        
class Cuenta:
    def __init__(self, numeroCuenta, saldo):
        self.numeroCuenta = numeroCuenta
        self.saldo = 0
    
    def CrearNumeroCuenta(self):
        self.numeroCuenta = random.randint(1000000, 9999999)
        
    def Depositar(self, monto):
        
        self.saldo += monto
        
def opciones():
    print("1. Agregar Persona")
    print("2. Agregar Cuenta")
    print("3. Mostrar Depositar y Retirar")
    print("4. Mostrar Información de las Cuenta")
    print("5. Salir")
    
def opcion():
    opcion = int(input("Seleccione una opción: "))
    return opcion
        
Personas = []
while True:
    print("_______// Menú //_______")
    opciones()
    opcionSeleccionada = opcion()
    if opcionSeleccionada == 1:
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        persona = Persona(nombre, edad)
        Personas.append(persona)
        print(f"Persona {nombre} agregada exitosamente.")
    elif opcionSeleccionada == 2:
        nombre = input("Ingrese el nombre del titular de la cuenta: ")
        for persona in Personas:
            cuenta = Cuenta(0, 0)
            cuenta.CrearNumeroCuenta()
        for persona in Personas:
            persona.agregarCuenta(cuenta)
            print(f"Cuenta creada para {persona.nombre}.")
                
    elif opcionSeleccionada == 3:
        for persona in Personas:
            print(f"Información de {persona.nombre}:")
            for cuenta in persona.cuenta:
                print(f"Número de Cuenta: {cuenta.numeroCuenta}, Saldo: ${cuenta.saldo}")
                monto = float(input("Ingrese el monto a depositar: "))
                cuenta.Depositar(monto)
                print(f"Nuevo saldo de la cuenta {cuenta.numeroCuenta}: ${cuenta.saldo}")
        
    elif opcionSeleccionada == 4:
        for persona in Personas:
            print(f"Información de {persona.nombre}:")
            for cuenta in persona.cuenta:
                print(f"Número de Cuenta: {cuenta.numeroCuenta}, Saldo: ${cuenta.saldo}")

    elif opcionSeleccionada == 5:
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.")
    