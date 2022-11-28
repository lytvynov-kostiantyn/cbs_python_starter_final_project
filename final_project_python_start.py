import random
from time import sleep
import pyjokes
from pyfiglet import Figlet
from random import choice
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
    'Some fun:)': ['ASCII art', 'Funny jokes']
}


def rock_paper_scissors():
    print('Welcome to the "rock-paper-scissors"'.center(60, ' '))
    print('If you want stop, press "q". Good luck!'.center(60, ' '))
    deliver()

    computer = 0
    user = 0

    while True:
        options = ['rock', 'paper', 'scissors']
        
        computer_choice = random.choice(options)
        user_input = input('Your choice: ').lower().strip()

        if user_input == 'q':
            print(f'Score: Computer {computer}:{user} User'.center(60, ' '))
            deliver()
            break
        
        if user_input not in options:
            print('Invalid input')
        else:
            if user_input == computer_choice:
                print('Draw!'.center(60, ' '))
            elif user_input == 'rock':
                if computer_choice == 'paper':
                    computer += 1
                else:
                    user += 1
            elif user_input == 'paper':
                if computer_choice == 'scissors':
                    computer += 1
                else:
                    user += 1
            else:
                if computer_choice == 'rock':
                    computer += 1
                else:
                    user += 1
            
            print(f'Score: Computer {computer}:{user} User'.center(60, ' '))
            deliver()


def guess_the_number():
    print('Welcome to the "guess the number"'.center(60, ' '))
    print('I guess the number in range 1...7, and you must'.center(60, ' '))
    print('guess it! If you want stop, press "q". Good luck!'.center(60, ' '))
    deliver()

    computer = 0
    user = 0

    while True:
        boo = random.randrange(1, 7)
        user_input = input('Your choice: ')
        if user_input.lower().strip() == 'q':
            print(f'Score: Computer {computer}:{user} User'.center(60, ' '))
            deliver()
            break
        try:
            baz = int(user_input)
        except ValueError:
            print('Invalid input')
            continue
        sleep(2)
        deliver()
        if baz == boo:
            print('You win!'.center(60, ' '))
            user += 1
        else:
            print('You lose!'.center(60, ' '))
            computer += 1
        
        print(f'Score: Computer {computer}:{user} User'.center(60, ' '))
        deliver()
        

# Getting genre from user and checking it in db
def get_genre(db_list, phrase='Input'):
    while True:
        genre_list = list(map(str.lower, db_list))
        genre = input(f'{phrase}: ').strip().lower()
        if genre in genre_list:
            return genre
        else:
            print('Invalid input')


# Getting menu number from user in special range
def get_menu_num(num, phrase='Input'):
    while True:
        try:
            x = int(input(f'{phrase}: '))
        except ValueError:
            print('Invalid input')
        else:
            if 1 <= x <= num:
                return x 


def deliver():
    print('-' * 60)


def main():
    while True:
        # Main menu
        print('Welcome cbs bot!'.center(60, '_'))
        print('Select one of available options: ')
        menu = list(catalog.keys())
        for i in range(len(menu)):
            print(f'\t{i + 1}. {menu[i]};')
        deliver()

        # Getting menu number from user
        user_input = get_menu_num(len(menu), 'Select menu number')
        deliver()

        if user_input in [1, 2, 3]:
            print('Available genre: ')
            match user_input:
                case 1:
                    baz = 'Recommend movie'
                case 2:
                    baz = 'Recommend music'
                case 3:
                    baz = 'Recommend pc game'

            db_genre_list = catalog[baz].keys()
            for key in db_genre_list:
                print(f'\t- {key};')
            deliver()

            # Getting genre from user
            genre = get_genre(db_genre_list, 'Genre name')

            # Giving the user a random movie from the database
            db_list = catalog[baz][genre]
            print('We can recommend: "{}"'.format(*random.choices(db_list)))
            deliver()

        elif user_input == 4:
            print('We can play: ')
            available_games = catalog['Play the game']
            for i in range(len(available_games)):
                print(f"\t{i + 1}. {available_games[i]};")
            deliver()

            # Getting menu number from user
            game_num = get_menu_num(len(available_games), 'Select game number')
            deliver()
            
            if game_num == 1:
                guess_the_number()
            else:
                rock_paper_scissors()
        
        elif user_input == 5:
            print('We can suggest: ')
            options = catalog['Some fun:)']
            for i in range(len(options)):
                print(f"\t{i + 1}. {options[i]};")
            deliver()

            # Getting menu number from user
            option_input = get_menu_num(len(options), 'xxx')
            deliver()

            if option_input == 1:
                print(pyjokes.get_joke())
                deliver()
            else:
                fonts_list = Figlet().getFonts()

                user_input = input('Phrase to convert: ')
                Figlet().setFont(font=choice(fonts_list))
                set_color = choice(['red', 'blue', 'yellow'])
                termcolor.cprint(Figlet().renderText(user_input), set_color)
                deliver()


if __name__ == '__main__':
    main()
