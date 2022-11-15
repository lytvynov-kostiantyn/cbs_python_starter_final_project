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


def main():
    while True:
        print('Hello:)')
        for key in catalog.keys():
            print(f'- {key};')
        break


if __name__ == '__main__':
    main()
