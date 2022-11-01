from filter_lines import ROCKYOU_FILENAME, filter_lines
from pympler import asizeof
from randomfile import RandomFile
from username import User

name = input("Enter your name: ")

print(User(username=name))

search = input("Enter a search word: ")

file_text = []
counter = 0

for searchs in filter_lines(ROCKYOU_FILENAME, search):
    file_text.append(searchs)
    counter += 1


class MyFile(RandomFile):
    file = open(RandomFile.file_to_create, "w")
    file.write("\n".join(file_text))
    size_file = asizeof.asizeof(RandomFile.file_to_create)


print(f"Total lines of file: {counter}")
# print(f"Total size of file: {MyFile.size_file}")
print("Total size of file: %d bytes" % MyFile.size_file)
