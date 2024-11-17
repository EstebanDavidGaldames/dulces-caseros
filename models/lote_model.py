#from datetime import datetime

from config import INVENTARIO_PATH
from file_helpers import write_json_file, read_json_file
#from dulce import Dulce
#from frasco import Frasco
#from produccion import Produccion

#class Lote(Dulce, Frasco, Produccion):
class Lote:
    all : list['Lote'] = []

    def __init__(self, fruta, frasco, cantidad, año):
        self.fruta = fruta
        self.frasco = frasco
        self.cantidad = cantidad
        self.año = año
        #self.tiempo = tiempo

        '''
        super().__init__(fruta)
        Frasco.__init__(self, tipo, cantidad)
        Produccion.__init__(self, año, tiempo)
        '''

    @classmethod
    def save(cls):
        write_json_file(INVENTARIO_PATH, [lote_obj.__dict__ for lote_obj in cls.all])
    
    @classmethod
    def load(cls):
        for lote in read_json_file(INVENTARIO_PATH):
            lote_obj = Lote(fruta=lote['fruta'], frasco=lote['frasco'], cantidad=lote['cantidad'], año=lote['año']) # tiempo=lote['tiempo'])
            cls.all.append(lote_obj)

    '''
    @property
    def tiempo(self):
        hoy = datetime.now()
        año_actual = hoy.year
        return (año_actual - self.año)
    '''

    def __str__(self):
        return f'{self.fruta} - {self.frasco} - {self.cantidad} - {self.año}' # {self.tiempo}
    