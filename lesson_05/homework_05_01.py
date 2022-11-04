from colors import Colors

"""
    Создайте контекстный менеджер colorizer,
    который будет печатать заданным цветом в произвольном блоке кода.
    После выхода из блока текст печатается обычным образом
"""


class Colorizer:
    color = {
        "grey": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "pink": "\033[95m",
        "turquoise": "\033[96m",
        "ENDC": "\033[0m",
    }

    def __init__(self, colorizer):
        self.color = colorizer

    def __enter__(self):
        if self.color in Colorizer.color:
            for key, value in Colorizer.color.items():
                if key == self.color:
                    break
            print(f"{value}", end="")
        else:
            print(f"{Colors.FAIL}Error color")
            self.color = Colorizer.color["ENDC"]

    def __exit__(self, type, value, traceback):
        print(f"{Colors.ENDC}", end="")


with Colorizer("red"):
    print("printed in red")
print("printed in default color")
