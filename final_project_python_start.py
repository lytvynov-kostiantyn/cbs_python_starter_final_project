import random

catalog = {
    'Recommend movie': {
        'comedies': ['1+1', 'Hangover', 'Bruce Almighty'],
        'horrors': ['Resident Evil', 'Paranormal Activity', 'Insidious'],
        'adventures': ['The Lord of the Rings', 'Matrix', 'Avengers'],
    },
    'Recommend music': {
        'heavy metal': ['Metallica - Enter Sandman', 'Ozzy Osbourne - Crazy Train', 'Slipknot - Duality'],
        'rap and hip-hop': ['Jelly Roll - Save Me', 'Nicki Minaj - Super Freaky Girl', 'Dax - JOKER'],
        'pop': ['Rihanna - Lift Me Up', 'Taylor Swift - Anti-Hero', 'Rihanna - Born Again'],
    },
    'Recommend pc game': {
        'shooters ': ['Halo', 'Gears of War', 'DOOM'],
        'sandbox': ['Minecraft', 'Grand Theft Auto', 'The Sims'],
        'strategy ': ['Warcraft', 'Age of Empires', 'Command & Conquer'],
    },
    'Play the game': ["Guess the number", "Rock-paper-scissors"],
}


# Getting integer from user
def get_int(phrase='Input'):
    while True:
        try:
            x = int(input(f'{phrase}: '))
            return x
        except ValueError:
            print('Invalid input')


def main():
    while True:
        # Main program menu
        print('Hello, select the option in the menu: ')
        menu_counter = 1
        for key in catalog.keys():
            print(f'\t{menu_counter}. {key};')
            menu_counter += 1

        # Getting integer from user
        user_input = get_int('Select menu number')
        print(user_input)
        break


if __name__ == '__main__':
    main()
