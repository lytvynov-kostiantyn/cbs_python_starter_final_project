from time import sleep
import pyjokes
from pyfiglet import Figlet
from random import choice, randrange, choices
import termcolor


catalog = {
    'Recommend movie': {
        'comedies': ['1+1', 'Hangover', 'Bruce Almighty'],
        'horrors': ['Resident Evil', 'Paranormal Activity', 'Insidious'],
        'adventures': ['The Lord of the Rings', 'Matrix', 'Avengers'],
    },
    'Recommend music': {
        'heavy metal': ['Metallica - Enter Sandman', 'Ozzy Osbourne - Crazy Train', 'Slipknot - Duality'],
        'hip-hop': ['Jelly Roll - Save Me', 'Nicki Minaj - Super Freaky Girl', 'Dax - JOKER'],
        'pop': ['Rihanna - Lift Me Up', 'Taylor Swift - Anti-Hero', 'Rihanna - Born Again'],
    },
    'Recommend pc game': {
        'shooters': ['Halo', 'Gears of War', 'DOOM'],
        'sandbox': ['Minecraft', 'Grand Theft Auto', 'The Sims'],
        'strategy': ['Warcraft', 'Age of Empires', 'Command & Conquer'],
    },
    'Play the game': ["Guess the number", "Rock-paper-scissors"],
    'More fun:)': ['Funny jokes', 'ASCII art'],
    'Exit': 'Exit'
}

colors = ['red', 'blue', 'yellow', 'green']


def rock_paper_scissors(name: str):
    print('Welcome to the "rock-paper-scissors"'.center(60, ' '))
    print('If you want to stop, press "q". Good luck!'.center(60, ' '))
    separator()

    computer = 0
    user = 0

    while True:
        options = ['rock', 'paper', 'scissors']
        
        computer_choice = choice(options)
        user_choice = input('Your choice: ').lower().strip()
        print(f'Computer choice: {computer_choice}')

        if user_choice == 'q':
            separator()
            print(f'Score: Computer {computer}:{user} {name}'.center(60, ' '))
            separator()
            sleep(3)
            break
        
        if user_choice not in options:
            print('Invalid input')
        else:
            separator()

            # Function to determine the winner
            def winner_determiner(var1, var2):
                if var1 == var2:
                    return 'Draw'
                if var1 == 'rock':
                    return 'User2' if var2 == 'paper' else 'User1'
                if var1 == 'paper':
                    return 'User2' if var2 == 'scissors' else 'User1'
                if var1 == 'scissors':
                    return 'User2' if var2 == 'rock' else 'User1'

            winner = winner_determiner(user_choice, computer_choice)
            if winner == 'Draw':
                print('Draw!'.center(60, ' '))
            elif winner == 'User1':
                print('You win!'.center(60, ' '))
                user += 1
            else:
                print('You lose!'.center(60, ' '))
                computer += 1

            print(f'Score: Computer {computer}:{user} {name}'.center(60, ' '))
            separator()


def guess_the_number(name: str):
    print('Welcome to the "guess the number"'.center(60, ' '))
    print('You must guess the number in the range from 1 to 7!'.center(60, ' '))
    print('If you want to stop, press "q". Good luck!'.center(60, ' '))
    separator()

    computer = 0
    user = 0

    while True:
        boo = randrange(1, 7)
        user_input = input('Your choice: ')
        if user_input.lower().strip() == 'q':
            separator()
            print(f'Score: Computer {computer}:{user} {name}'.center(60, ' '))
            separator()
            sleep(3)
            break
        try:
            baz = int(user_input)
        except ValueError:
            print('Invalid input')
            continue
        sleep(2)
        separator()
        if baz == boo:
            print('You win!'.center(60, ' '))
            user += 1
        else:
            print('You lose!'.center(60, ' '))
            computer += 1
        
        print(f'Score: Computer {computer}:{user} {name}'.center(60, ' '))
        separator()


# Getting genre from user and checking it in db
def get_genre(db_list: list, phrase='Input'):
    while True:
        genre_list = list(map(str.lower, db_list))
        genre = input(f'{phrase}: ').strip().lower()
        if genre in genre_list:
            return genre
        else:
            print('Invalid input')


# Getting menu number from user in special range
def get_menu_num(num: int, phrase='Input'):
    while True:
        try:
            x = int(input(f'{phrase}: '))
        except ValueError:
            print('Invalid input')
        else:
            if 1 <= x <= num:
                return x
            else:
                print('Invalid input')


# Procedure for design
def separator():
    set_color = choice(colors)
    termcolor.cprint('-' * 60, set_color)


def main():
    while True:
        # Main menu
        print('Welcome cbs bot!'.center(60, '.'))
        print('Select one of available options: ')
        menu = list(catalog.keys())
        for i in range(len(menu)):
            print(f'\t{i + 1}. {menu[i]};')
        separator()

        # Getting menu number from user
        user_input = get_menu_num(len(menu), 'Select menu number')
        separator()

        if user_input in [1, 2, 3]:
            print('Available genres: ')
            match user_input:
                case 1:
                    baz = 'Recommend movie'
                case 2:
                    baz = 'Recommend music'
                case 3:
                    baz = 'Recommend pc game'

            db_genre_list = catalog[baz].keys()
            for key in db_genre_list:
                print(f'\t- {key.capitalize()};')
            separator()

            # Getting genre from user
            genre = get_genre(db_genre_list, 'Genre name')

            # Giving the user a random movie from the database
            db_list = catalog[baz][genre]
            separator()
            print('We can recommend: "{}"'.format(*choices(db_list)))
            separator()
            sleep(3)

        elif user_input == 4:
            print('We can play: ')
            available_games = catalog['Play the game']
            for i in range(len(available_games)):
                print(f"\t{i + 1}. {available_games[i]};")
            separator()

            # Getting menu number from user
            game_num = get_menu_num(len(available_games), 'Select game number')
            separator()

            user_name = input('Enter your name: ')
            boo = user_name if user_name else 'User'

            if game_num == 1:
                guess_the_number(boo)
            else:
                rock_paper_scissors(boo)
        
        elif user_input == 5:
            print('We can suggest: ')
            options = catalog['More fun:)']
            for i in range(len(options)):
                print(f"\t{i + 1}. {options[i]};")
            separator()

            # Getting menu number from user
            option_input = get_menu_num(len(options), 'Select menu number')
            separator()

            if option_input == 1:
                print(pyjokes.get_joke())
                separator()
                sleep(3)
            else:
                # Getting fonts from module
                fonts_list = Figlet().getFonts()
                # Getting phrase from user for converting
                user_input = input('Phrase to convert: ')
                # Setting random font
                Figlet().setFont(font=choice(fonts_list))
                # Setting random color
                set_color = choice(colors)
                # Printing result
                termcolor.cprint(Figlet().renderText(user_input), set_color)
                separator()
                sleep(3)

        else:
            print('Goodbye!'.center(60, ' '))
            separator()
            break


if __name__ == '__main__':
    main()
