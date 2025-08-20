inventario={
    "cuaderno":15,
    "lapiz":40,
    "marcador":10,
    "borrador":0,
    "regla":5
}


while True:
    print("**Menu**\n1. Agregar producto\n2. Vender\n3. Ver inventario")
    seleccion=int(input("Ingrese su eleccion: "))
    if seleccion==1:
        nombre=input("Ingrese el nombre del producto: ").lower
        cantidad=int(input("Ingrese la cantidad a agregar: "))
        if nombre in inventario:
            inventario[nombre]=cantidad
        else:
            inventario[nombre]+=cantidad
    elif seleccion==2:
        nombre=input("Ingrese el nombre del producto: ").lower
        if nombre in inventario:
            cantidad =int(input("ingrese la cantidad que desea vender: "))
            if cantidad <= inventario[nombre]:
                inventario[nombre]-= cantidad
            else:
                print("No hay inventario")
    elif seleccion==3:
        print(inventario)
    

           
        