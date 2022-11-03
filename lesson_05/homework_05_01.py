from colors import Colors

""" Создайте контекстный менеджер colorizer,
    который будет печатать заданным цветом в произвольном блоке кода.
    После выхода из блока текст печатается обычным образом
"""

color = {
    "grey": "\033[90m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "pink": "\033[95m",
    "red": "\033[91m",
    "turquoise": "\033[96m",
}


class Colorizer:
    def __init__(self, colorizer):
        if colorizer in color:
            self.color = colorizer
        else:
            print(f"{Colors.FAIL}Error color")
            self.color = "ENDC"

    def __enter__(self):
        for key, value in color.items():
            if key == self.color:
                break
        print(f"{value}", end="")

    def __exit__(self, type, value, traceback):
        print(f"{Colors.ENDC}", end="")


with Colorizer("red"):
    print("printed in red")
print("printed in default color")
