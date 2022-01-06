from package import GameCell


class GameMap:

    __height, __width = 0, 0
    map = []

    def __init__(self, first_generation):
        self.__height = first_generation.size[1]
        self.__width = first_generation.size[0]
        self.map = [[GameCell.GameCell() for _i in range(self.__width)] for _j in range(self.__height)]
