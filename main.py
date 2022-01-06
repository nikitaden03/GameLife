import argparse
from package import GameControl

game_control = None


def alert_window():
    input(
        "Первое поколение должно быть в формате jpg. Белый цвет - мертвые клетки, черный - живые. \nНичего страшного," +
        " если изображение будет содержать небольшие шумы или тени, программа пострается исправить их.\n" +
        "Нажмите Enter, чтобы продолжить")


def parse_args():
    global game_control

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input_file", required=True)
    parser.add_argument("--output", dest="output_folder", required=True)
    parser.add_argument("--max_iter", dest="max_iter", default=0)
    parser.add_argument("--dump_freq", dest="dump_freq", default=1)

    args = parser.parse_args()
    game_control = GameControl.GameControl(args.input_file, args.output_folder, args.max_iter, args.dump_freq)


def main():
    alert_window()
    parse_args()


if __name__ == "__main__":
    main()
