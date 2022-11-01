import os
import random
from pathlib import Path

# from pympler import asizeof


os.chdir("./lesson_04/search_file")


class RandomFile:
    file_name = random.randint(1, 50)
    file_to_create = str(file_name) + ".txt"
    Path(file_to_create).touch()
    # size_file = asizeof.asizeof(file_to_create)


file = RandomFile
# print(f"Total size of file: {RandomFile.size_file}")
