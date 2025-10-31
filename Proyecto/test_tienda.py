import pytest
import os
from Tienda import TiendaMascotas
from Productos import Productos
from Mascotas import Perros, Gatos, Pez, Pajaro
from Usuarios import Usuarios
from Excepciones import ItemNoEncontradoError

def test_inicializacion_tienda():
    tienda = TiendaMascotas("Mi Tienda", "Calle Falsa 123")
    assert tienda.nombre == "Mi Tienda"
    assert tienda.direccion == "Calle Falsa 123"
    assert len(tienda.getProductos()) == 0
    assert len(tienda.getMascotas()) == 0
    assert len(tienda.getClientes()) == 0

def test_agregar_y_listar_items():
    tienda = TiendaMascotas("TestShop", "Calle Test")
    producto = Productos("Pelota", 10.0, "Juguete")
    mascota = Perros("Firulais", 2, 100.0)
    cliente = Usuarios("Ana")

    tienda.AgregarProducto(producto)
    tienda.AgregarMascota(mascota)
    tienda.AgregarCliente(cliente)

    assert producto in tienda.getProductos()
    assert mascota in tienda.getMascotas()
    assert cliente in tienda.getClientes()
    assert len(tienda.getProductos()) == 1
    assert len(tienda.getMascotas()) == 1
    assert len(tienda.getClientes()) == 1

def test_vender_producto_exitoso(capsys):
    tienda = TiendaMascotas("TestShop", "Calle Test")
    producto = Productos("Hueso", 5.0, "Accesorio")
    tienda.AgregarProducto(producto)
    usuario = Usuarios("Luis")
    tienda.AgregarCliente(usuario)

    pid = producto.getId()
    tienda.VenderProducto(usuario, pid)

    assert producto in usuario.GetListaProductos
    assert producto in tienda.getProductos()

    captured = capsys.readouterr()
    assert "Venta exitosa" in captured.out

def test_vender_producto_no_encontrado():
    tienda = TiendaMascotas("TestShop", "Calle Test")
    usuario = Usuarios("Maria")
    with pytest.raises(ItemNoEncontradoError):
        tienda.VenderProducto(usuario, "P99999")

def test_vender_mascota_exitosa(capsys):
    tienda = TiendaMascotas("TestShop", "Calle Test")
    mascota = Gatos("Michi", 1, 150.0)
    tienda.AgregarMascota(mascota)
    usuario = Usuarios("Carlos")

    mid = mascota.getId()
    tienda.VenderMascota(usuario, mid)

    assert mascota in usuario.GetListaMascotas
    assert mascota not in tienda.getMascotas()

    captured = capsys.readouterr()
    assert "Venta exitosa" in captured.out

def test_vender_mascota_no_encontrada():
    tienda = TiendaMascotas("TestShop", "Calle Test")
    usuario = Usuarios("Laura")
    with pytest.raises(ItemNoEncontradoError):
        tienda.VenderMascota(usuario, "M99999")

def test_mostrar_productos_vacios(capsys):
    tienda = TiendaMascotas("Tienda Vacía", "Ahora Mismo")
    tienda.MostrarProductos()
    captured = capsys.readouterr()
    assert "El inventario de productos está vacío" in captured.out

def test_mostrar_historial_ventas_vacio(capsys):
    tienda = TiendaMascotas("Tienda sin Clientes", "En la Esquina")
    tienda.MostrarHistorialVentas()
    captured = capsys.readouterr()
    assert "No hay clientes registrados" in captured.out
