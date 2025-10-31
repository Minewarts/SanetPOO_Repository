import pytest
import re
from Mascotas import Perros, Gatos, Pez, Pajaro
from Excepciones import EdadInvalidaError

def test_atributos_perro():
    perro = Perros('Generico', 5, 3.01)
    assert perro.nombre == 'Generico'
    assert perro.edad == 5
    assert perro.precio == 3.01

def test_atributos_gato():
    gato = Gatos('Generico', 2, 1.50)
    assert gato.nombre == 'Generico'
    assert gato.edad == 2
    assert gato.precio == 1.50

def test_mascota_generacion_id():
    perro = Perros('Generico', 5, 3.01)
    gato = Gatos('Generico', 2, 1.50)
    id_perro = perro.getId()
    id_gato = gato.getId()

    assert isinstance(id_perro, str)
    assert re.fullmatch(r"M\d{5}", id_perro)
    assert re.fullmatch(r"M\d{5}", id_gato)
    assert id_perro != id_gato


def test_edad_invalida_lanza_excepcion():
    with pytest.raises(EdadInvalidaError) as excinfo:
        Perros('Boby', -1, 5.0)
    mensaje_error = str(excinfo.value)
    # Se usa "in" para evitar errores si el mensaje exacto cambia
    assert "no es válida" in mensaje_error
    assert "Debe ser un número positivo" in mensaje_error

def test_perros_hacer_sonido(capsys):
    perro = Perros('Generico', 5, 3.01)
    perro.HacerSonido()
    captured = capsys.readouterr()
    assert "Generico hace guau guau" in captured.out.strip()

def test_gatos_hacer_sonido(capsys):
    gato = Gatos('Generico', 2, 3.01)
    gato.HacerSonido()
    captured = capsys.readouterr()
    assert "Generico hace miau miau" in captured.out.strip()

def test_pez_pajaro_hacer_sonido(capsys):
    pez = Pez("Nemo", 1, 1.00)
    pajaro = Pajaro("Piolin", 3, 2.00)

    pez.HacerSonido()
    pajaro.HacerSonido()

    captured = capsys.readouterr().out.strip().splitlines()

    assert any("Nemo hace glu glu" in line for line in captured)
    assert any("Piolin hace pio pio" in line for line in captured)
    
#si no funciona pytest: python -m pytest --cov=.