# from colorama import Fore, Style


class Colors:
    """цветной текст: диапазон 90-96"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[90m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[92m"
    BOLD = "\033[96m"

    """ цвета фона текста: диапазон 100-107"""
    GREYBG = "\033[100m"
    REDBG = "\033[101m"
    GREENBG = "\033[102m"
    YELLOWBG = "\033[103m"
    BLUEBG = "\033[104m"
    PINKBG = "\033[105m"
    CYANBG = "\033[106m"

    """ эффекты шрифта """
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    # Background colors:
    GREYBG = "\033[100m"
    REDBG = "\033[101m"
    GREENBG = "\033[102m"
    YELLOWBG = "\033[103m"
    BLUEBG = "\033[104m"
    PINKBG = "\033[105m"
    CYANBG = "\033[106m"


# print(f'{Colors.OKGREEN}{"Hello"}{Colors.ENDC}, {"Andrii"}')
# print(f'{Bcolors.GREENBG}{"Hello"}{Bcolors.ENDC}, {"Andrii"}')
# print(f'{Fore.RED}{"Hello"}{Style.RESET_ALL}, {"Andrii"}')


# class ColorsPrint:
#     print("\033[21m", end="")
#     print("wer")
#     print("\033[1m", end="")
#     print("wer")
#     print("\033[3m", end="")
#     print("wer")
#     print("\033[4m", end="")
#     print("wer")

#     print("\033[90m", end="")
#     print("qwe0")
#     print("\033[91m", end="")
#     print("qwe1")
#     print("\033[92m", end="")
#     print("qwe2")
#     print("\033[93m", end="")
#     print("qwe3")
#     print("\033[94m", end="")
#     print("qwe4")
#     print("\033[95m", end="")
#     print("qwe5")
#     print("\033[96m", end="")
#     print("qwe6")

#     print("\033[100m", end="")
#     print("qwe0")
#     print("\033[101m", end="")
#     print("qwe1")
#     print("\033[102m", end="")
#     print("qwe2")
#     print("\033[103m", end="")
#     print("qwe3")
#     print("\033[104m", end="")
#     print("qwe4")
#     print("\033[105m", end="")
#     print("qwe5")
#     print("\033[106m", end="")
#     print("qwe6")
