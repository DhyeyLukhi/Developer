import pyfiglet
from termcolor import colored
import random


def colors(statement):
    colors = ["red", "green", "yello", "blue", "cyan", "white"]
    ascii_art = pyfiglet.figlet_format(text=statement, font="slant")
    print(colored(ascii_art, color=random.choice(colors)))


statement = input("Statement: ")
colors(statement)
