import random
class Persona:
    def __init__(self, nombre, numeros):
        self.nombre=nombre
        self.numeros=[random.randint(100,999) for _ in range (0,5)]



listaDePersonas=[]
while True:
    print("-----||----- Menu -----||-----")
    print("1. Añadir participante")
    print("2. Ver numeros participantes")
    print("3. Ver ganador")
    print("4. Salir")
    seleccion=int(input("Ingrese su opcion: "))
    if seleccion==1:
        personaAdd=Persona(input("Ingrese su nombre"))
        listaDePersonas.append(Persona)
    elif(seleccion==2):
        print(listaDePersonas)
    elif(seleccion==3):

        for i in range(0, random.randint(0, len(listaDePersonas)-1)):
            ganador=listaDePersonas[i]
        print(f'El ganador es {ganador}')
    elif(seleccion==4):
        break
    else:
        print("Opcion Invalida")
            





        
