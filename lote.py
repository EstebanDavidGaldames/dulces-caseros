from dulce import Dulce
from frasco import Frasco
from produccion import Produccion

class Lote(Dulce, Frasco, Produccion):
    def __init__(self, fruta, tipo, cantidad, año, tiempo):
        super().__init__(fruta)
        Frasco.__init__(self, tipo, cantidad)
        Produccion.__init__(self, año, tiempo)

    def __str__(self):
        return f'{self.fruta} - {self.tipo} - {self.cantidad} - {self.año} - {self.tiempo}'

#lote_prueba = Lote('durazno', 'chico común', '660 cc', 30, 2018, tiempo_de_almacenamiento='')
#lote_prueba_1 = Lote('uva', 'hexagonal', '666', 40, 2022, tiempo_de_almacenamiento='')

lote_prueba = Lote('durazno', 'chico común', 30, 2018, tiempo='')
lote_prueba_1 = Lote('uva', 'hexagonal', 40, 2022, tiempo='')

print(lote_prueba)
print(lote_prueba_1)

print(lote_prueba.fruta)
print(lote_prueba_1.fruta)

print(lote_prueba.tipo)
print(lote_prueba_1.tipo)

#print(lote_prueba.capacidad)
#print(lote_prueba_1.capacidad)
