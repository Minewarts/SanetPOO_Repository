class Estudiante:
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
        print("Opcion no valida")

    
    
