import os
import random

from pympler import asizeof

lst = [
    "rockyou",
    " rockstar",
    "rockon",
    "rocker",
    "rocky",
    "rockme",
    "rocku",
    "therock",
    "rocky1",
    "yourock",
    "rock you",
    " punkrock",
    "rockyou1",
    "rocknroll",
    "rocket",
    "ROCKYOirockRockYou",
    "rockers",
    "shamrock",
    "rockstar1",
    "rockyou!",
    "rocks",
    "hardrock",
]
os.chdir("./lesson_04/search_file")


class SizeFile:
    def __init__(self, file_text) -> None:
        randomfile = open(str(random.randint(1, 50)) + ".txt", "w")
        randomfile.write("\n".join(file_text))
        self.randomfile = randomfile

    def __str__(self) -> str:
        return str(asizeof.asizeof(self.randomfile))


sizefile = SizeFile(lst)
print(f"Total size of file: {sizefile}")
