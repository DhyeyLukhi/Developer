from colorama import Fore

print(Fore.RED + "Hello World")
print(Fore.LIGHTCYAN_EX + "Hello world")

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Example usage
print(color.RED + 'This is red text!' + color.END)
print(color.GREEN + 'This is green text!' + color.END)
print(color.BOLD + 'This is bold text!' + color.END)
print(color.UNDERLINE + 'This is underlined text!' + color.END)
