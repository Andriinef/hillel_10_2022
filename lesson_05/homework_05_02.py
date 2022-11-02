class Resource:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Colorizer:
    def __init__(self, color):
        self.__resource = Resource(color)

    def __enter__(self):
        return self.__resource

    def __exit__(self, type, value, traceback):
        self.__resource.get_color()


with Colorizer("red"):
    print("printed in red")
print("printed in default color")
