#from datetime import datetime

#from core.data_input import get_tiempo

class Produccion:
    def __init__(self, año, tiempo):
        self.año = año
        self.tiempo = tiempo

    #def set_tiempo(self):
    #    tiempo = get_tiempo()
    #    return self.tiempo - self.año
    
    #@property
    #def año_de_produccion(self):
    #    return self._año_de_produccion
    
    #@año_de_produccion.setter
    #def año_de_produccion(self, año):
    #    self._año_de_produccion = año
    
    #@property
    #def tiempo(self):
    #    hoy = datetime.now()
    #    año_actual = hoy.year
    #    return (año_actual - self.año)
