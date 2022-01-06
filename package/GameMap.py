from package import GameCell


class GameMap:

    __height, __width = 0, 0
    map = []

    def __init__(self, first_generation):
        self.__height = first_generation.size[1]
        self.__width = first_generation.size[0]
        colors = {}

        for j in range(self.__height):
            self.map.append([])
            for i in range(self.__width):
                self.map[j].append(GameCell.GameCell())
                color = first_generation.getpixel((i, j))
                if color != (255, 255, 255) and color != (0, 0, 0):
                    if abs(255 - color[0]) < abs(0 - color[0]) or color == (255, 255, 255):
                        first_generation.putpixel((i, j), (255, 255, 255))
                    else:
                        first_generation.putpixel((i, j), (0, 0, 0))
                color = first_generation.getpixel((i, j))
                if color in colors:
                    colors[color] += 1
                else:
                    colors[color] = 1
        print(colors)
