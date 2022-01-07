import os.path
from PIL import Image
from package.GameMap import GameMap


class GameControl:

    _input_file, _output_folder, _max_iter, _dump_freq = "", "", 0, 0

    def __init__(self, input_file, output_folder, max_iter, dump_freq):
        self._input_file = input_file.strip()
        self._output_folder = output_folder.strip()
        self._max_iter = max_iter.strip()
        self._dump_freq = dump_freq
        self.game_map = None
        self.init_map()

    def init_map(self):

        if not (os.path.exists(self._input_file) and os.path.isfile(self._input_file)):
            print(f"К сожалению, {self._input_file} не существует или не является файлом!")
            exit(0)
        if list(self._input_file.split("."))[-1] != "png":
            print(f"Файл с первым поколением игры должен быть в формате png!")
            exit(0)

        self.game_map = GameMap(Image.open(self._input_file).convert("RGB"))
