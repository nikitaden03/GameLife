import argparse
from package import GameControl


def alert_window():
    input(
        "Первое поколение должно быть в формате png. Белый цвет - мертвые клетки, черный - живые.\n" +
        "Нажмите Enter, чтобы продолжить")


def parse_args():
    """
    Функция разбирает аргументы комндной строки, создает объект класса GameControl
    и передает в качестве стартовых параметров распарсенные аргументы
    :return: Ранее созданный объект класса GameControl
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input_file", required=True)
    parser.add_argument("--output", dest="output_folder", required=True)
    parser.add_argument("--max_iter", dest="max_iter", default=0)
    parser.add_argument("--dump_freq", dest="dump_freq", default=1)

    args = parser.parse_args()
    game_control = GameControl.GameControl(args.input_file, args.output_folder, int(args.max_iter), int(args.dump_freq))

    return game_control


def main():
    alert_window()
    game_control = parse_args()
    game_control.prepare_folder()
    game_control.play_game()


if __name__ == "__main__":
    main()
