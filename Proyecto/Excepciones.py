class ErrorBaseTienda(Exception):
    """Clase base para las excepciones específicas de la tienda."""
    pass

class ItemNoEncontradoError(ErrorBaseTienda):
    """Excepción lanzada cuando un producto o mascota no se encuentra por su ID."""
    def __init__(self, item_id: str, tipo_item: str):
        self.item_id = item_id
        self.tipo_item = tipo_item
        super().__init__(f"No se encontró {self.tipo_item} con el ID: {self.item_id}")

class EspecieInvalidaError(ErrorBaseTienda):
    """Excepción lanzada cuando la especie ingresada no es válida."""
    def __init__(self, especie: str):
        self.especie = especie
        super().__init__(f"La especie '{self.especie}' no es una especie válida.")

class EntradaInvalidaError(ErrorBaseTienda):
    """Excepción lanzada cuando la entrada del usuario no tiene el formato esperado (ej. esperar un número y recibir texto)."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        
class EdadInvalidaError(ErrorBaseTienda):
    """Excepción lanzada cuando la edad ingresada no es un valor positivo o lógico."""
    def __init__(self, edad: int):
        self.edad = edad
        super().__init__(f"La edad '{self.edad}' no es válida. Debe ser un número positivo.")
