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
        print('Hello, available options: ')
        menu_counter = 1
        for key in catalog.keys():
            print(f'\t{menu_counter}. {key.capitalize()};')
            menu_counter += 1
        menu_counter = 1

        # Getting menu number from user
        while True:
            menu_input = get_int('\nSelect menu number')
            if menu_input in range(1, len(catalog.keys()) + 1):
                break
            else:
                print('Invalid input')

        match menu_input:
            case 1:
                print('\nAvailable movie genre: ')
                for key in catalog['Recommend movie'].keys():
                    print(f'\t- {key.capitalize()};')

                # Getting movie genre from user
                while True:
                    genre_list = list(map(str.lower, catalog['Recommend movie'].keys()))
                    movie_genre = input('\nGenre name: ').strip().lower()
                    if movie_genre in genre_list:
                        break
                    else:
                        print('Invalid input')

                # Giving the user a random movie from the database
                movie_list = catalog['Recommend movie'][movie_genre]
                print('We can recommend: "{}"'.format(*random.choices(movie_list)))
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

        break


if __name__ == '__main__':
    main()
