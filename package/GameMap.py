import GameCell


class GameMap:

    __height, __width = 0, 0
    map = []

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.map = [[GameCell.GameCell() for _i in range(width)] for _j in range(height)]
