import random

def roll_dice(num_dices):
    print('Use from [sample] package folder...')
    return [random.randint(1, 6) for x in range(0, num_dices)]