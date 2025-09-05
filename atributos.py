'''class Persona:
    def __init__(self, nombre,cedula, TI):
        self.nombre=nombre
        self.__cedula=cedula
        self.__TI=TI

    def ObtenerDoc(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__TI

persona1=Persona("Juana",1111,None)
persona2=Persona("Jose",2222,None)
niño1=Persona("Kaiyu",None,3333)

print(persona1.nombre, persona1.ObtenerDoc())
print(persona2.nombre, persona2.ObtenerDoc())
print(niño1.nombre, niño1.ObtenerDoc())'''

class Casa:
    def __init__(self, direccion):
        self.direccion=direccion
        self.__espacios=[]

    def AgregarEspacio(self,nombre):
        self.__espacios.append(Espacio(nombre))

    def MostrarEspacio(self):
        for espacio in self.__espacios:
            print(espacio.tipoEspacio)

    def BuscarEspacio(self, nombre):
        for espacio in self.__espacios:
            if espacio.tipoEspacio==nombre:
                return espacio
        return None

class Espacio:
    def __init__(self, tipoEspacio):
        self.tipoEspacio=tipoEspacio
        self.__dispositivos=[]

    def AgregarDispositivos(self, Dispositivo):
        self.__dispositivos.append(Dispositivo)

    def MostrarDispositivos(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombreDispositivo)


class Dispositivo:
    def __init__(self,nombreDispositivo):
        self.nombreDispositivo=nombreDispositivo
        self.__estado=False

    def CambiarEstado(self):
        if self.__estado is True:
            self.__estado=False
            print("Apagando Dispositivo")
        else:
            self.__estado=True
            print("Encendiendo Dispositivo")


myHouse=Casa("Calle 66")
myHouse.AgregarEspacio("Cocina")
myHouse.AgregarEspacio("Habitacion")
myHouse.AgregarEspacio("Baño")

dispositivo1=Dispositivo("Horno")

myHouse.BuscarEspacio("Cocina").AgregarDispositivos(dispositivo1)

myHouse.BuscarEspacio("Cocina").MostrarDispositivos()

myHouse.MostrarEspacio()
        