# Proyecto Tienda de Mascotas Entregable
# Sanet Correa Castaño, Jhairo Esteban Muñeton Cortes
# 2025-2

from Tienda import TiendaMascotas
from Productos import Productos
from Mascotas import Pez,Gatos,Perros,Pajaro
from Usuarios import Usuarios
from Excepciones import ItemNoEncontradoError, EspecieInvalidaError, EntradaInvalidaError

tienda = TiendaMascotas("C++cotas","Calle 123")
try:
    tienda.CargarDatos()
except Exception:
    pass

print("Bienvenido a nuestra tienda")
print(tienda.nombre, "Direccion: ", tienda.direccion)


especiesValidas = {
    "Perro": Perros,
    "Gato": Gatos,
    "Pez": Pez,
    "Pajaro": Pajaro
}

while True:
    print("\n------------------------------------")
    print("seleccione la opcion deseada")
    print("1. Agregar mercancia")
    print("2. Agregar mascota")
    print("3. Mostrar Productos")
    print("4. Mostrar Mascotas")
    print("5. Vender Producto")
    print("6. Vender Mascota")
    print("7. Mostrar Historial de ventas")
    print("8. Mostrar Mascotas Compradas por Usuario")
    print("0. Salir")
    print("------------------------------------")
    
    try:
        opcion_str = input("Ingrese su opcion: ")
        
        if not opcion_str.isdigit():
            raise EntradaInvalidaError("La opción del menú debe ser un número entero.")
            
        opcion = int(opcion_str)

        if opcion == 1:
            nombre = input("ingresa El nombre del producto: ").capitalize()
            for producto in tienda.getProductos():
                if producto.nombre == nombre:
                    print("El producto ya existe en la tienda. No se agregará.")
                    break
            else:
                try:
                    precio = float(input("ingresa el precio del producto: "))
                except ValueError:
                    raise EntradaInvalidaError("El precio debe ser un número válido.")
                    
                tipo = input("ingresa el tipo de producto (Alimento, Juguete, Accesorio): ").capitalize()
                
                producto = Productos(nombre, precio, tipo) 
                tienda.AgregarProducto(producto)
                print("Se ha añadido el producto exitosamente")
            
        elif opcion == 2:
            nomMascota = input("Ingrese el nombre de la mascota: ").capitalize()
            especieMascota = input("Ingrese la especie de la mascota (Perro, Gato, Pez, Pajaro): ").capitalize()
            
            if especieMascota not in especiesValidas:
                raise EspecieInvalidaError(especieMascota)

            try:
                edadMascota = int(input("Ingrese la edad de la mascota: "))
            except ValueError:
                raise EntradaInvalidaError("La edad de la mascota debe ser un número entero positivo.")
            
            try:
                precioMascota = float(input("Ingrese el precio de la mascota: "))
            except ValueError:
                raise EntradaInvalidaError("El precio de la mascota debe ser un número válido.")
                    
            for mascota in tienda.getMascotas():
                if mascota.nombre == nomMascota and mascota.especie == especieMascota:
                    print("Una mascota con ese nombre y especie ya existe en la tienda.")
                    break
            else:
                ClaseMascota = especiesValidas[especieMascota]
                mascota = ClaseMascota(nomMascota, edadMascota, precioMascota)
                tienda.AgregarMascota(mascota)
                print("Se ha añadido la mascota exitosamente")
                    
        elif opcion == 3:
            tienda.MostrarProductos() 

        elif opcion == 4:
            if not tienda.getMascotas():
                print("No hay mascotas en la tienda")
            else:
                print("Mascotas disponibles en la tienda:")
                for mascota in tienda.getMascotas():
                    mascota.MostrarInfo()
                    
        elif opcion == 5:
            nombre = input("Ingrese su nombre: ").capitalize()
            usuario = None
            
            for i in tienda.getClientes():
                if i.nombre == nombre:
                    print("El cliente ya existe en la tienda, proceda con su compra")
                    usuario = i
                    break
            
            if usuario is None:
                usuario = Usuarios(nombre)
                tienda.AgregarCliente(usuario)
                print("Se ha añadido el cliente exitosamente")

            if not tienda.getProductos():
                print("No hay productos en la tienda")
            else:
                print("Productos disponibles en la tienda:")
                tienda.MostrarProductos() 
                
                idProducto = input("Ingrese el ID del producto que desea comprar: ")
                
                tienda.VenderProducto(usuario, idProducto)
                    
        elif opcion == 6:
            nombre = input("Ingrese su nombre: ").capitalize()
            usuario = None
            
            for i in tienda.getClientes():
                if i.nombre == nombre:
                    print("El cliente ya existe en la tienda, proceda con su compra")
                    usuario = i
                    break
            
            if usuario is None:
                usuario = Usuarios(nombre)
                tienda.AgregarCliente(usuario)
                print("Se ha añadido el cliente exitosamente")

            if not tienda.getMascotas():
                print("No hay mascotas en la tienda")
            else:
                print("Mascotas disponibles en la tienda:")
                for mascota in tienda.getMascotas():
                    mascota.MostrarInfo()
                    
                idMascota = input("Ingrese el ID de la mascota que desea comprar: ")
                
                tienda.VenderMascota(usuario, idMascota)
                    
        elif opcion == 7:
            tienda.MostrarHistorialVentas() 

        elif opcion == 8:
            nombre = input("Ingrese su nombre: ").capitalize()
            usuario = None
            for i in tienda.getClientes():
                if i.nombre == nombre:
                    usuario = i
                    break
            if usuario:
                usuario.MostrarMascotas()
            else:
                print("El cliente no existe en la tienda")
                
        elif opcion == 0:
            try:
                tienda.ActualizarBasesDatos()
            except Exception:
                pass
            print("Gracias por visitar. Saliendo del programa.")
            break
        
        else:
            raise EntradaInvalidaError(f"Opción de menú '{opcion}' no válida. Ingrese un número del 0 al 8.")

    except EntradaInvalidaError as e:
        print("\n--- ERROR DE ENTRADA ---")
        print(f"ERROR: {e}")
        print("Asegúrese de ingresar números donde se soliciten y el formato sea correcto.")
        print("------------------------")
    
    except EspecieInvalidaError as e:
        print("\n--- ERROR DE ESPECIE ---")
        print(f"ERROR: {e}")
        print("Las especies válidas son: Perro, Gato, Pez, Pajaro.")
        print("------------------------")
        
    except ItemNoEncontradoError as e:
        print("\n--- ERROR DE COMPRA ---")
        print(f"ERROR: {e}")
        print("Verifique el ID en el inventario e intente de nuevo.")
        print("-----------------------")
        
    except Exception as e:
        print("\n--- ERROR INESPERADO DEL SISTEMA ---")
        print(f"Ocurrió un error no manejado: {e}")
        print("------------------------------------")