from filter_lines import ROCKYOU_FILENAME, filter_lines
from pympler import asizeof
from username import User
import random
import os


os.chdir("./lesson_04/search_file")

name = input("Enter your name: ")

print(User(username=name))

search = input("Enter a search word: ")

file_text = []
counter = 0

for searchs in filter_lines(ROCKYOU_FILENAME, search):
    file_text.append(searchs)
    counter += 1


class SizeFile:
    def __init__(self) -> None:
        randomfile = open(str(random.randint(1, 50)) + ".txt", "w")
        randomfile.write("\n".join(file_text))
        self.randomfile = randomfile

    def __str__(self) -> str:
            return str(asizeof.asizeof(self.randomfile))



sizefile = SizeFile()
print(f"Total lines of file: {counter}")
print(f"Total size of file: {sizefile}")
