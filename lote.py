from dulce import Dulce
from frasco import Frasco
from produccion import Produccion

class Lote(Dulce, Frasco, Produccion):
    def __init__(self, fruta, tipo, capacidad, cantidad, año_de_produccion, tiempo_de_almacenamiento):
        super().__init__(fruta)
        Frasco.__init__(self, tipo, capacidad, cantidad)
        Produccion.__init__(self, año_de_produccion, tiempo_de_almacenamiento)

    def __str__(self):
        return f'{self.fruta} - {self.tipo} - {self.capacidad} - {self.cantidad} - {self.año_de_produccion} - {self.tiempo_de_almacenamiento}'

lote_prueba = Lote('durazno', 'chico común', '660 cc', 30, 2018, tiempo_de_almacenamiento='')
lote_prueba_1 = Lote('uva', 'hexagonal', '666', 40, 2022, tiempo_de_almacenamiento='')

print(lote_prueba)
print(lote_prueba_1)

print(lote_prueba.fruta)
print(lote_prueba_1.fruta)

print(lote_prueba.tipo)
print(lote_prueba_1.tipo)

print(lote_prueba.capacidad)
print(lote_prueba_1.capacidad)
