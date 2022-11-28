import pyjokes
from pyfiglet import Figlet
from random import choice
import termcolor

# Jokes module
print(pyjokes.get_joke())

# Art module
figlet = Figlet()
fonts_list = figlet.getFonts()

user_input = input('Phrase to convert: ')
figlet.setFont(font=choice(fonts_list))
set_color = choice(['red', 'blue', 'yellow'])
termcolor.cprint(figlet.renderText(user_input), set_color)
