class Empleado:
    def __init__(self, nombre, documento, edad):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    
    def getDocumento(self):
        return self.__documento
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDocumento(self, documento):
        self.__documento = documento

    def setEdad(self, edad):
        self.__edad = edad
    
    def MostrarInfo(self):
        return {"nombre": self.__nombre, "documento": self.__documento, "edad": self.__edad}
    
class Desarrollador(Empleado):
    def __init__(self, nombre, documento, edad, tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def MostrarInfo(self):
        info = super().MostrarInfo()
        info["tipo"] = self.__tipo
        return info
    
class Gerente(Empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area = area
        self.__empleadosACargo = []

    def getArea(self):
        return self.__area
    
    def setArea(self, area):
        self.__area = area

    def AñadirEmpleado(self, empleado):
        self.__empleadosACargo.append(empleado)

    def MostrarEmpleados(self):
        for empleado in self.__empleadosACargo:
            print(empleado.MostrarInfo())
    
    def MostrarInfo(self):
        info = super().MostrarInfo()
        info["area"] = self.__area
        return info
    

empleado = Desarrollador("Jhairo", 123456789, 30, "Backend")
empleado1 = Desarrollador("Ana Gomez", 987654321, 28, "Testing")
empleado2 = Desarrollador("Luis Martinez", 456789123, 35, "Frontend")
gerente = Gerente("Sanet", 9999999999, 18, "TICS")

gerente.AñadirEmpleado(empleado)
gerente.AñadirEmpleado(empleado1)
gerente.AñadirEmpleado(empleado2)
gerente.MostrarEmpleados()