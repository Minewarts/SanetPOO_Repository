#Listas
'''import random 

listaRandom= [random.random() for _ in range(10)]

print(listaRandom)'''
#Funciones
listaEjemplo= [i for i in range(10)]
print(listaEjemplo)
listaEjemplo[2]=10
listaEjemplo[5]=2
listaEjemplo.remove(3)
print (listaEjemplo)
#Remover por posicion

del listaEjemplo[2]
print(listaEjemplo)

listaEjemplo.append(1)
print (listaEjemplo)

listaEjemplo=[elemento for elemento in listaEjemplo if elemento!=1]
print(listaEjemplo)
listaEjemplo.sort()
print(listaEjemplo)
listaEjemplo.sort(reverse=True)
print(listaEjemplo)
listaEjemplo.reverse
print(listaEjemplo)