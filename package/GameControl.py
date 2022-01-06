class GameControl:

    _input_file, _output_folder, _max_iter, _dump_freq = "", "", 0, 0

    def __init__(self, input_file, output_folder, max_iter, dump_freq):
        self._input_file = input_file
        self._output_folder = output_folder
        self._max_iter = max_iter
        self._dump_freq = dump_freq
