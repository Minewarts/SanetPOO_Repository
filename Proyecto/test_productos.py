import pytest
from Productos import Productos

def test_producto_inicializacion():
    producto = Productos(nombre="Croquetas", precio=150.50, tipo="Alimento")
    assert producto.nombre == "Croquetas"
    assert producto.precio == 150.50
    assert producto.tipo == "Alimento"

def test_producto_generacion_id():
    producto1 = Productos("Pelota", 50.0, "Juguete")
    producto2 = Productos("Collar", 75.0, "Accesorio")

    id1 = producto1.getId()
    id2 = producto2.getId()

    assert isinstance(id1, str)
    assert id1 != id2
    assert id1.startswith("P")
    assert len(id1) == 6
    assert id1[1:].isdigit()

def test_producto_mostrar_info(capsys):
    producto = Productos("Arena", 200.0, "Accesorio")
    producto.MostrarInfo()
    captured = capsys.readouterr()
    output = captured.out

    assert producto.id_producto in output
    assert "Arena" in output
    assert "$200.00" in output
    assert "Accesorio" in output

def test_producto_to_formato_csv():
    producto = Productos("Pescado", 10.0, "Alimento")
    csv_data = producto.toFormatoCsv()
    assert csv_data == [producto.id_producto, "Pescado", "10.0", "Alimento"]