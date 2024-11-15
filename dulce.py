class Dulce:
    def __init__(self, fruta):
        self._fruta = fruta

    @property
    def fruta(self):
        return self._fruta
    
    @fruta.setter
    def fruta(self, fruto):
        self._fruta = fruto
