class Ponto:
    def __init__(self, x, y):
        self._x, self._y = x, y
    
    def __str__(self):
        return f'({self._x, self._y})'