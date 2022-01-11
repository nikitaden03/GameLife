"""
    Класс, управляющие ходом игры, запускает инициализацию игрового поля, управляет генерированием и сохранением новых
    поколений, а также останавливает игру, когда достигаются нужные условия
"""

import os.path
import shutil
from PIL import Image
from package.GameMap import GameMap


class GameControl:
    _input_file, _output_folder, _max_iter, _dump_freq = "", "", 0, 0

    __hash_set = {}

    def __init__(self, input_file, output_folder, max_iter, dump_freq):
        self._input_file = input_file.strip()
        self._output_folder = output_folder.strip()
        self._max_iter = max_iter
        self._dump_freq = dump_freq
        self.__game_map = None
        self.order = 0
        self.__frames = []
        self.init_map()

    def init_map(self):
        """
        Функция проверяет, что передано корректное изображение в качестве первого поколения, и запускает инициализацию
        игрового поля
        """
        if not (os.path.exists(self._input_file) and os.path.isfile(self._input_file)):
            print(f"К сожалению, {self._input_file} не существует или не является файлом!")
            exit(0)
        if list(self._input_file.split("."))[-1] != "png":
            print(f"Файл с первым поколением игры должен быть в формате png!")
            exit(0)
        if os.path.exists(self._output_folder) and os.path.isfile(self._output_folder):
            print("--output должен содержать путь к директории. Если директории по данному пути не сущствует она ",
                  "будет создана, иначе все содержимое будет безвозвратно удалено!")
            exit(0)

        self.__game_map = GameMap(Image.open(self._input_file).convert("RGB"))

    def prepare_folder(self):
        """
        Если требуется, очищает папку, в которой будут лежать новые поколения
        """
        if os.path.exists(self._output_folder):
            shutil.rmtree(self._output_folder)
        os.mkdir(self._output_folder)

    def __generate_label(self):
        """
        Генерирует путь нового поколения, имеющему вид "путь к папке/Generation - номер поколения"
        :return: путь к новому поколению
        """
        self.order += 1
        return self._output_folder + "/" + "Generation - " +  str(self.order) + ".png"

    def __save_generation(self):
        """
        Сохраняет новое поколение в формате rgb
        """
        generation = Image.new('RGB', (self.__game_map.get_width(), self.__game_map.get_height()), 'white')
        game_map = self.__game_map.get_map()
        for j in range(self.__game_map.get_height()):
            for i in range(self.__game_map.get_width()):
                if game_map[j][i].get_is_alive():
                    generation.putpixel((i, j), (0, 0, 0))
        label = self.__generate_label()
        generation.save(label)
        self.__frames.append(Image.open(label).convert("RGB"))

    def play_game(self):
        """
        Управляет ходом игры; когда игра подойдет к концу, запускает сохранение гиф-изображения
        """
        i = 0
        while i < self._max_iter or self._max_iter == 0:
            hash_obj = self.__game_map.get_hash()
            if hash_obj in self.__hash_set:
                break
            self.__hash_set[hash_obj] = True
            self.__game_map.next_generation()
            if i % self._dump_freq == 0:
                self.__save_generation()
            i += 1
        self.__save_gif()

    def __save_gif(self):
        """
        Сохраняет гиф-изображение
        """
        self.__frames[0].save(
            self._output_folder + "/" + "Generation.gif",
            save_all=True,
            append_images=self.__frames[1:],
            optimize=True,
            duration=20,
            loop=0
        )