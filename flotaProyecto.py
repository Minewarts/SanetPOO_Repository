class Flota:
    def __init__(self):
        self.__autos=[]
        
    def AgregarAuto(self,auto):
        for autoi in self.__autos:
            if autoi.placa == auto.placa:
                print("Auto ya existe")
                return
        self.__autos.append(auto)
        print("Auto agregado exitosamente")
        
    def QuitarAuto(self,placa):
        for autoi in self.__autos:
            if autoi.placa == placa:
                self.__autos.remove(autoi)
                print("Auto removido")
                return
        print("Auto no encontrado")
            
    def BuscarAuto(self,placa):
        for autoi in self.__autos:
            if autoi.placa == placa:
                autoi.MostrarInfo()
                return autoi
        print("Auto no encontrado")
        return None  

    def MostrarReporte(self):
        print ("Reporte de autos en la flota")
        print (f'Auto    --   Estado   -- Total: {len(self.__autos)}')
        for autoi in self.__autos:
            autoi.MostrarInfo()
                
                
class Auto:
    def __init__(self,modeloVehiculo,caballos, modelo):
        self.modeloVehiculo = modeloVehiculo
        self.__placa = None
        
        self.__motor = Motor(modelo, int(caballos))
        self.servicio = "Disponible"

   
    @property
    def placa(self):
        return self.__placa
    
    def ColocarPlaca(self,placa):
        self.__placa = placa
    
    def MostrarInfo(self):
        print(f"Placa: {self.__placa} -- Modelo: {self.modeloVehiculo} -- Motor/Estado: {self.__motor.estado} -- Servicio: {self.servicio}")
        
    def CambiarEstado(self):
        if self.servicio == "Disponible":
            self.servicio = "En servicio"
        else:
            self.servicio = "Disponible"
        print("Cambiando estado de servicio...")

    
    def EncenderApagarMotor(self):
        self.__motor.EncenderApagar()

        
class Motor:
    def __init__(self,modelo,caballos):
        self.__modelo = modelo
        self.__caballos = caballos
        self.estado = "Apagado"
        
    def EncenderApagar(self):
        if self.estado == "Encendido":
            self.estado = "Apagado"
            print("Apagando motor")
        else:
            self.estado = "Encendido"
            print("Encendiendo motor")



flota = Flota()
while True:
    print("-----||----- Menu -----||-----")
    print("1. Agregar auto")
    print("2. Quitar auto")
    print("3. Buscar auto")
    print("4. Mostrar reporte")
    print("5. Cambiar estado de auto (Disponible/En servicio)")
    print("6. Encender/Apagar motor")
    print("7. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        modeloVehiculo = input("Ingrese el modelo del vehiculo: ")
        caballos = input("Ingrese los caballos de fuerza: ")
        modeloMotor = input("Ingrese el modelo del motor: ")
        placa = input("Ingrese la placa del vehiculo: ")
        autoNuevo = Auto(modeloVehiculo, caballos, modeloMotor)
        autoNuevo.ColocarPlaca(placa)
        flota.AgregarAuto(autoNuevo)

    elif opcion == "2":
        placa = input("Ingrese la placa del vehiculo a quitar: ")
        flota.QuitarAuto(placa)

    elif opcion == "3":
        placa = input("Ingrese la placa del vehiculo a buscar: ")
        flota.BuscarAuto(placa)

    elif opcion == "4":
        flota.MostrarReporte()

    elif opcion == "5":
        placa = input("Ingrese la placa del vehiculo a cambiar de estado: ")
        auto_encontrado = flota.BuscarAuto(placa)
        if auto_encontrado:              
            auto_encontrado.CambiarEstado()

    elif opcion == "6":
        placa = input("Ingrese la placa del vehiculo: ")
        auto_encontrado = flota.BuscarAuto(placa)
        if auto_encontrado:               
            auto_encontrado.EncenderApagarMotor()  

    elif opcion == "7":
        break

    else:
        print("Opcion no valida, intente de nuevo")