class ItemNoEncontradoError(Exception):
    """Excepción lanzada cuando una mascota o producto no se encuentra por su ID."""
    def __init__(self, item_id: str, tipo: str):
        self.item_id = item_id
        self.tipo = tipo
        super().__init__(f"No se encontró {tipo} con el ID: {item_id}")

class EspecieInvalidaError(Exception):
    """Excepción lanzada cuando se intenta crear una mascota con una especie no reconocida."""
    def __init__(self, especie: str):
        self.especie = especie
        super().__init__(f"Especie de mascota inválida: {especie}")

class EntradaInvalidaError(Exception):
    """Excepción base para manejar entradas de usuario que no son válidas."""
    pass