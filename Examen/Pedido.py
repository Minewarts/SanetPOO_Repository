class linea_pedido:
    def __init__(self,nombre,cant,peso):
        self.nombre=nombre
        self.peso=peso
        self.cant=cant

class Pedido:
    def __init__(self,destinatario,distancia,):
        self.destinatario=destinatario
        self.distancia=distancia
        self.lista_lineas=[]

    def AgregarLinea(self,nombre,cant,peso):
        self.lista_lineas.append(linea_pedido(nombre,cant,peso))

    def CalcularTotal(self):
        total=0
        for linea in self.lista_lineas:
            total+=linea.peso*linea.cant
        return total
    


