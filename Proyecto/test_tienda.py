import pytest
from Tienda import TiendaMascotas
from Productos import Productos
from Mascotas import Perros, Gatos
from Usuarios import Usuarios
from Excepciones import ItemNoEncontradoError

def test_agregar_y_listas_basico():
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

def test_vender_producto_exitoso(capsys):
    tienda = TiendaMascotas("TestShop", "Calle Test")
    producto = Productos("Hueso", 5.0, "Accesorio")
    tienda.AgregarProducto(producto)
    usuario = Usuarios("Luis")
    tienda.AgregarCliente(usuario)

    pid = producto.getId()
    tienda.VenderProducto(usuario, pid)

    lista_prod_usuario = usuario.GetListaProductos
    assert any((p is producto) for p in lista_prod_usuario)
    assert all(p is not producto for p in tienda.getProductos())

    captured = capsys.readouterr()
    assert "Venta" in captured.out or "venta" in captured.out or "compró" in captured.out

def test_vender_producto_no_encontrado():
    tienda = TiendaMascotas("TestShop", "Calle Test")
    usuario = Usuarios("Maria")
    tienda.AgregarCliente(usuario)
    with pytest.raises(ItemNoEncontradoError):
        tienda.VenderProducto(usuario, "P99999")

def test_vender_mascota_exitoso(capsys):
    tienda = TiendaMascotas("TestShop", "Calle Test")
    mascota = Perros("Rex", 3, 200.0)
    tienda.AgregarMascota(mascota)
    usuario = Usuarios("Carlos")
    tienda.AgregarCliente(usuario)

    mid = mascota.getId()
    tienda.VenderMascota(usuario, mid)

    lista_mascotas_usuario = usuario.GetListaMascotas
    assert any((m is mascota) for m in lista_mascotas_usuario)
    assert all(m is not mascota for m in tienda.getMascotas())

    captured = capsys.readouterr()
    assert "Venta" in captured.out or "compró" in captured.out

def test_vender_mascota_no_encontrado():
    tienda = TiendaMascotas("TestShop", "Calle Test")
    usuario = Usuarios("Laura")
    tienda.AgregarCliente(usuario)
    with pytest.raises(ItemNoEncontradoError):
        tienda.VenderMascota(usuario, "M99999")

def test_mostrar_productos_y_historial(capsys):
    tienda = TiendaMascotas("TestShop", "Calle Test")
    p1 = Productos("Croquetas", 120.0, "Alimento")
    p2 = Productos("Arena", 200.0, "Accesorio")
    m1 = Gatos("Michi", 2, 80.0)
    tienda.AgregarProducto(p1)
    tienda.AgregarProducto(p2)
    tienda.AgregarMascota(m1)
    u = Usuarios("Pedro")
    tienda.AgregarCliente(u)

    tienda.VenderProducto(u, p1.getId())
    tienda.VenderMascota(u, m1.getId())

    tienda.MostrarProductos()
    tienda.MostrarHistorialVentas()

    captured = capsys.readouterr()
    out = captured.out

    assert "Croquetas" in out or "Croquetas" in out
    assert "Michi" in out or "Michi" in out
    assert "ha comprado" in out or "compró" in out