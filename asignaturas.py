class GrupoAsignatura:
    def __init__(self,nombre,horario,profesor,grupo):
        self.nombre=nombre
        self.horario=horario
        self.grupo=grupo
        self.profesor=profesor
        self.estudiantes=[]
    
    def AgregarEstudiantes(self,estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante Agregado exitosamente")

    def CalcularPromedio(self):
        suma=0
        for estudiante in self.estudiantes:
            suma=suma+estudiante.nota
        promedio=suma/len(self.estudiantes)
        return promedio
    
    def MostrarEstudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)

    
class Profesor:
    def __init__(self,nombre,edad,experiencia):
        self.nombre=nombre
        self.edad=edad
        self.experiencia=experiencia

class Estudiante:
    def __init__(self,nombre,edad,nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota

    
listaDeGrupos=[]
idContador=0
while True:
    idContador+= idContador
    #Menu
    print("----/--Menu--/----")
    print("1. Añadir nueva asignatura\n2. Añadir un estudiante al grupo\n3. mostrar promedio de los grupos\n4. Salir")
    opcion = int(input("Ingrese su opcion numerica: "))
    if opcion==1:
        print("Primero ingrese el profesor del grupo")
        profesor=Profesor(input("Ingrese el nombre del profesor: "),int(input("Ingrese la edad del profesor: ")),int(input("Ingrese los años de experiencia del profesor: ")))
        print("Ahora ingrese los demas datos del grupo")
        nombre=input("Ingrese el nombre del grupo: ")
        horario=input("Ingrese el horario del grupo: ")
        grupo=GrupoAsignatura(nombre,horario,profesor,idContador)
    elif opcion==2:
        print("Ingrese")
