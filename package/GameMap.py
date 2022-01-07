from package import GameCell


class GameMap:
    __height, __width = 0, 0
    __map = []

    def __init__(self, first_generation):
        self.__height = first_generation.size[1]
        self.__width = first_generation.size[0]
        colors = {}

        for j in range(self.__height):
            self.__map.append([])
            for i in range(self.__width):
                self.__map[j].append(GameCell.GameCell())
                color = first_generation.getpixel((i, j))
                if color in colors:
                    colors[color] += 1
                else:
                    colors[color] = 1

        if len(colors) > 2:
            print(f"Изображение должно содержать не более двух цветов. В переданном - {len(colors)}!")
            exit(0)

        if not ((len(colors) == 2 and (255, 255, 255) in colors and (0, 0, 0) in colors) or (
                len(colors) == 1 and ((255, 255, 255) in colors or (0, 0, 0) in colors))):
            print("Изображение может сожержать только черные (0, 0, 0) и белые (255, 255, 255) цвета!")
            exit(0)

        for j in range(self.__height):
            for i in range(self.__width):
                if first_generation.getpixel((i, j)) == (255, 255, 255):
                    self.__map[j][i].set_is_alive = False
                else:
                    self.__map[j][i].set_is_alive = True
