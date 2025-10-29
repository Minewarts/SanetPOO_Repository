import pytest
import uuid
from Productos import Productos

def test_producto_inicializacion():
    """Prueba que los atributos del producto se inicializan correctamente."""
    producto = Productos(nombre="Croquetas", precio=150.50, tipo="Alimento")
    
    assert producto.nombre == "Croquetas"
    assert producto.precio == 150.50
    assert producto.tipo == "Alimento"

def test_producto_generacion_id():
    """Prueba que el ID se genera automáticamente, es un string y es único."""
    producto1 = Productos("Pelota", 50.0, "Juguete")
    producto2 = Productos("Collar", 75.0, "Accesorio")
    
    id1 = producto1.GetId()
    id2 = producto2.GetId()
    
    assert isinstance(id1, str)
    assert id1 != id2
    
    # Intenta validar que es un formato UUID
    try:
        uuid.UUID(id1)
        uuid_valido = True
    except ValueError:
        uuid_valido = False
    assert uuid_valido

def test_producto_mostrar_info(capsys):
    """Prueba que la función MostrarInfo imprime los datos correctos."""
    producto = Productos("Arena", 200.0, "Accesorio")
    producto.MostrarInfo()
    
    captured = capsys.readouterr()
    output = captured.out
    
    assert producto.id_producto in output
    assert "Arena" in output
    assert "$200.00" in output # Verifica el formato de precio
    assert "Accesorio" in output

def test_producto_to_formato_csv():
    """Prueba que el método de formato CSV devuelve la lista correcta."""
    producto = Productos("Pescado", 10.0, "Alimento")
    
    csv_data = producto.toFormatoCsv()
    
    # El precio debe ser un string en la lista
    assert csv_data == [producto.id_producto, "Pescado", "10.0", "Alimento"]
    