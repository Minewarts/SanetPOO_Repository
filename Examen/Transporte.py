from Pedido import Pedido

class Transporte: 
    def __init__(self,capacidad,velocidad):
        self.capacidad=capacidad
        self.velocidad=velocidad
        self.pedidos_acargo=[]

    def AsignarPedido(self,pedido):
        self.pedidos_acargo.append(pedido)

    def CalcularTiempo(self):
        ...

    def CalcularCosto(self):
        ...

class Bicicleta(Transporte):
    def __init__(self, capacidad=15, velocidad=20):
        super().__init__(capacidad, velocidad)
    def CalcularTiempo(self):
        distancia_total=0
        for i in self.pedidos_acargo:
            distancia_total+=i.distancia
        tiempo=distancia_total/self.velocidad
    def CalcularCosto(self):
        distancia_total=0
        for i in self.pedidos_acargo:
            distancia_total+=i.distancia
        costo=100+(100*0.2)*distancia_total



