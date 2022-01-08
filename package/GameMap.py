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
                self.__map[j].append(GameCell.GameCell(False))
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
                    self.__map[j][i].set_is_alive(False)
                else:
                    self.__map[j][i].set_is_alive(True)

    def count_neighbours(self, cell_x, cell_y):
        alive_neighbours = 0

        # if cell_x + 1 < self.__width:
        #     if cell_y - 1 >= 0 and self.__map[cell_y - 1][cell_x + 1].get_is_alive():
        #         alive_neighbours += 1
        #     if self.__map[cell_y][cell_x + 1].get_is_alive():
        #         alive_neighbours += 1
        #     if cell_y + 1 < self.__height and self.__map[cell_y + 1][cell_x + 1].get_is_alive():
        #         alive_neighbours += 1
        #
        # if cell_x - 1 >= 0:
        #     if cell_y - 1 >= 0 and self.__map[cell_y - 1][cell_x - 1].get_is_alive():
        #         alive_neighbours += 1
        #     if self.__map[cell_y][cell_x - 1].get_is_alive():
        #         alive_neighbours += 1
        #     if cell_y + 1 < self.__height and self.__map[cell_y + 1][cell_x - 1].get_is_alive():
        #         alive_neighbours += 1
        #
        # if cell_y - 1 >= 0 and self.__map[cell_y - 1][cell_x].get_is_alive():
        #     alive_neighbours += 1
        # if cell_y + 1 < self.__height and self.__map[cell_y + 1][cell_x].get_is_alive():
        #     alive_neighbours += 1

        if self.__map[(cell_y - 1) % self.__height][(cell_x + 1) % self.__width].get_is_alive():
            alive_neighbours += 1
        if self.__map[cell_y % self.__height][(cell_x + 1) % self.__width].get_is_alive():
            alive_neighbours += 1
        if self.__map[(cell_y + 1) % self.__height][(cell_x + 1) % self.__width].get_is_alive():
            alive_neighbours += 1

        if self.__map[(cell_y - 1) % self.__height][(cell_x - 1) % self.__width].get_is_alive():
            alive_neighbours += 1
        if self.__map[cell_y % self.__height][(cell_x - 1) % self.__width].get_is_alive():
            alive_neighbours += 1
        if self.__map[(cell_y + 1) % self.__height][(cell_x - 1) % self.__width].get_is_alive():
            alive_neighbours += 1

        if self.__map[(cell_y - 1) % self.__height][cell_x].get_is_alive():
            alive_neighbours += 1
        if self.__map[(cell_y + 1) % self.__height][cell_x].get_is_alive():
            alive_neighbours += 1

        return alive_neighbours

    def next_generation(self):
        new_map = []
        for j in range(self.__height):
            new_map.append([])
            for i in range(self.__width):
                count_neighbours = self.count_neighbours(i, j)
                if 2 <= count_neighbours <= 3 and self.__map[j][i].get_is_alive() or count_neighbours == 3 and \
                        not self.__map[j][i].get_is_alive():
                    is_alive = True
                else:
                    is_alive = False

                new_map[j].append(GameCell.GameCell(is_alive))
        self.__map = list(new_map)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_map(self):
        return self.__map
