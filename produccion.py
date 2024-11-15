from datetime import datetime

class Produccion:
    def __init__(self, año_de_produccion, tiempo_de_almacenamiento):
        self._año_de_produccion = año_de_produccion
        self._tiempo_de_almacenamiento = tiempo_de_almacenamiento

    @property
    def año_de_produccion(self):
        return self._año_de_produccion
    
    @año_de_produccion.setter
    def año_de_produccion(self, año):
        self._año_de_produccion = año
    
    @property
    def tiempo_de_almacenamiento(self):
        hoy = datetime.now()
        año_actual = hoy.year
        return (año_actual - self.año_de_produccion)
