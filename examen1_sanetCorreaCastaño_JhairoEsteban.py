class Libro:
    def __init__(self, titulo, autor, añoDePublicacion, genero):
        self.titulo=titulo
        self.autor=autor
        self.añoDePublicacion=añoDePublicacion
        self.genero=genero
    def MostrarDatos(self):
        print(self.titulo,"--",self.autor,"--",self.añoDePublicacion,"--",self.genero)


listaDeLibros=[]
while True:
    #Menu
    print("Menu")
    print("1. Registrar nuevos libros en la biblioteca.\n2. Mostrar todos los libros registrados.\n3. Consultar libros(Por Titulo)\n4. Salir")
    opcion = int(input("Ingrese su opcion: "))
    if opcion==1:
        tituloLibro=str(input("Ingrese el titulo del libro: "))
        autor=input("Ingrese el Autor: ")
        añoDePublicacion= int(input("Ingrese el año depublicacion: "))
        genero=input("Ingrese el genero del libro: ")
        libroNuevo=Libro(tituloLibro,autor,añoDePublicacion,genero)
        listaDeLibros.append(libroNuevo)
        print("Libro agregado correctamente")

    #Mostrar libros registrados 
    elif opcion == 2:
        print(f"Titulo / Autor / Año De Publicacion / Genero / Cantidad de libros = {len(listaDeLibros)}")
        for libros in listaDeLibros:
            libros.MostrarDatos()
    
    elif opcion == 3: 
        tituloLibro=str(input("Ingrese el titulo del libro: "))
        existe = False 
        for libros in listaDeLibros:
            if tituloLibro == libros.titulo:
                print(f"Titulo / Autor / Año De Publicacion / Genero")
                libros.MostrarDatos()
                existe= True
                break
        if existe == False:
            print("El libro no existe")

    elif opcion == 4:
        print("Hasta la vista BB")
        break

    else:
        print("Opcion invalida")

            
