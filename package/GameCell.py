"""
Класс, реализующий логику клетки игрового поля
"""

class GameCell:

    __is_alive = False

    def __init__(self, is_alive):
        self.__is_alive = is_alive

    def get_is_alive(self):
        return self.__is_alive

    def set_is_alive(self, is_alive):
        self.__is_alive = is_alive
