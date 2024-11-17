from config import INVENTARIO_PATH
from file_helpers import write_json_file, read_json_file


class Lote:
    all : list['Lote'] = []

    def __init__(self, fruta, frasco, cantidad, año):
        self.fruta = fruta
        self.frasco = frasco
        self.cantidad = cantidad
        self.año = año

    @classmethod
    def save(cls):
        write_json_file(INVENTARIO_PATH, [lote_obj.__dict__ for lote_obj in cls.all])
    
    @classmethod
    def load(cls):
        for lote in read_json_file(INVENTARIO_PATH):
            lote_obj = Lote(fruta=lote['fruta'], frasco=lote['frasco'], cantidad=lote['cantidad'], año=lote['año'])
            cls.all.append(lote_obj)

    def __str__(self):
        return f'{self.fruta} - {self.frasco} - {self.cantidad} - {self.año}'
    