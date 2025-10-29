import pytest
import uuid
from Mascotas import Perros, Gatos, Pez, Pajaro
from Excepciones import EdadInvalidaError 

def test_atributos_perro():
    perro = Perros('Generico', 5, 3.01)
    assert perro.nombre == 'Generico'
    assert perro.edad == 5
    assert perro.precio == 3.01

def test_atributos_gato():
    gato = Gatos('Generico', 2,1.50)
    assert gato.nombre == 'Generico'
    assert gato.edad == 2 
    assert gato.edad == 1.50

def test_mascota_generacion_id():
    perro = Perros('Generico', 5,3.01)
    gato = Gatos('Generico', 2,1.50)
    id_perro = perro.get_id()
    id_gato = gato.get_id()
    
    assert isinstance(id_perro, str)
    assert uuid.UUID(id_perro)
    assert id_perro != id_gato

def test_edad_invalida_lanza_excepcion():
    with pytest.raises(EdadInvalidaError) as excinfo:
        Perros('Boby', -1)
        
    assert "no puede ser negativa" in str(excinfo.value)
    
def test_perros_hacer_sonido(capsys):
    perro = Perros('Generico', 5,3.01)
    perro.hacer_sonido() 
    captured = capsys.readouterr()
    assert "Generico hace guau guau" in captured.out

def test_gatos_hacer_sonido(capsys):
    gato = Gatos('Generico', 2,3.01)
    gato.hacer_sonido() 
    captured = capsys.readouterr()
    assert "Generico hace miau miau" in captured.out
    
def test_pez_pajaro_hacer_sonido(capsys):
    pez = Pez("Nemo", 1,1.00) 
    pajaro = Pajaro("Piolin", 3,2.00)
    
    pez.hacer_sonido() 
    pajaro.hacer_sonido() 
    
    captured = capsys.readouterr()
    assert "Nemo hace glu glu" in captured.out
    assert "Piolin hace pío pío" in captured.out
    
#si no funciona pytest: python -m pytest --cov=.