class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[90m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[92m"
    BOLD = "\033[96m"
    ENDC = "\033[0m"


color = {
    "ENDC": "\033[0m",
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
