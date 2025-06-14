"""Cho-Han, by Al Sweigart al@inventwithpython.com
Modified by Scott Anderson for Module 3 assignment
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# saa: Updated game intro with bonus notice
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTE: If the dice roll totals 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # saa: Changed input prompt
        pot = input('saa: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        # saa: Changed input prompt
        bet = input('saa: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine outcome:
    total = dice1 + dice2
    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # saa: Bonus rule for rolling 2 or 7
    if total == 2 or total == 7:
        print(f'You rolled a {total}! Bonus: 10 mon added to your purse.')
        purse += 10

    # Results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        # saa: Updated house cut to 12%
        print('The house collects a', int(pot * 0.12), 'mon fee.')
        purse -= int(pot * 0.12)
    else:
        purse -= pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()




