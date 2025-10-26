import pytest
import uuid
from Proyecto.Mascotas import Perros, Gatos, Pez, Pajaro

@pytest.fixture
def perro_instance():
    """Fixture para crear una instancia de Perros."""
    return Perros("Max", 5, "Perro")

@pytest.fixture
def gato_instance():
    """Fixture para crear una instancia de Gatos."""
    return Gatos("Mishi", 2, "Gato")

def test_mascota_creacion_atributos(perro_instance):
    """Verifica la correcta inicialización de atributos de una mascota."""
    assert perro_instance.nombre == "Max"
    assert perro_instance.edad == 5
    assert perro_instance.especie == "Perro"

def test_mascota_generacion_id(perro_instance, gato_instance):
    """Verifica que el ID sea un UUID válido y único."""
    id_perro = perro_instance.GetId()
    id_gato = gato_instance.GetId()
    
    # 1. Es un string
    assert isinstance(id_perro, str)
    # 2. Es un UUID válido
    assert uuid.UUID(id_perro)
    # 3. Son diferentes
    assert id_perro != id_gato

def test_perros_hacer_sonido(perro_instance, capsys):
    """Verifica el método HacerSonido para Perros."""
    perro_instance.HacerSonido()
    captured = capsys.readouterr()
    assert "Max hace guau guau" in captured.out

def test_gatos_hacer_sonido(gato_instance, capsys):
    """Verifica el método HacerSonido para Gatos."""
    gato_instance.HacerSonido()
    captured = capsys.readouterr()
    assert "Mishi hace miau miau" in captured.out
    
def test_pez_pajaro_hacer_sonido(capsys):
    """Verifica los métodos HacerSonido para Pez y Pajaro."""
    pez = Pez("Nemo", 1, "Pez")
    pajaro = Pajaro("Piolin", 3, "Pajaro")
    
    pez.HacerSonido()
    pajaro.HacerSonido()
    
    captured = capsys.readouterr()
    assert "Nemo hace glu glu" in captured.out
    assert "Piolin hace pio pio" in captured.out