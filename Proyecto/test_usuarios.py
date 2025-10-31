import pytest
from Usuarios import Usuarios
from Productos import Productos
from Mascotas import Perros, Gatos

def test_usuario_inicializacion():
    usuario = Usuarios("Carlos")
    assert usuario.nombre == "Carlos"
    assert usuario.GetListaProductos == []
    assert usuario.GetListaMascotas == []

def test_agregar_producto():
    usuario = Usuarios("Ana")
    producto1 = Productos("Collar", 25.0, "Accesorio")
    producto2 = Productos("Pelota", 10.0, "Juguete")

    usuario.AgregarProducto(producto1)
    usuario.AgregarProducto(producto2)

    lista = usuario.GetListaProductos
    assert len(lista) == 2
    assert lista[0].nombre == "Collar"
    assert lista[1].precio == 10.0

def test_agregar_mascota():
    usuario = Usuarios("Juan")
    perro = Perros("Boby", 3, 150.0)
    gato = Gatos("Michi", 2, 120.0)

    usuario.AgregarMascota(perro)
    usuario.AgregarMascota(gato)

    lista = usuario.GetListaMascotas
    assert len(lista) == 2
    assert lista[0].nombre == "Boby"
    assert lista[1].nombre == "Michi"

def test_mostrar_compras_sin_productos(capsys):
    usuario = Usuarios("Luis")
    usuario.MostrarCompras()
    captured = capsys.readouterr()
    assert "no ha comprado nada" in captured.out

def test_mostrar_compras_con_productos(capsys):
    usuario = Usuarios("Sofía")
    producto = Productos("Correa", 50.0, "Accesorio")
    usuario.AgregarProducto(producto)
    usuario.MostrarCompras()
    captured = capsys.readouterr()
    assert "ha comprado" in captured.out
    assert "Correa" in captured.out
    assert "$50.0" in captured.out

def test_mostrar_mascotas_sin_mascotas(capsys):
    usuario = Usuarios("Marcos")
    usuario.MostrarMascotas()
    captured = capsys.readouterr()
    assert "no ha comprado mascotas" in captured.out

def test_mostrar_mascotas_con_mascotas(capsys):
    usuario = Usuarios("Laura")
    perro = Perros("Toby", 4, 180.0)
    usuario.AgregarMascota(perro)
    usuario.MostrarMascotas()
    captured = capsys.readouterr()
    assert "ha comprado las siguientes mascotas" in captured.out
    assert "Toby" in captured.out
