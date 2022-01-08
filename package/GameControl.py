import os.path
import shutil
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
        self.order = 0
        self.init_map()

    def init_map(self):
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

        self.game_map = GameMap(Image.open(self._input_file).convert("RGB"))

        self.generate_number()
        self.generate_number()

    def prepare_folder(self):
        if os.path.exists(self._output_folder):
            shutil.rmtree(self._output_folder)
        os.mkdir(self._output_folder)

    def generate_number(self):
        self.order += 1
        return self._output_folder + "/" + str(self.order)

    def safe_generation(self):
        pass
