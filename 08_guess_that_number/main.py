# %%
from typing import Final
import random

# Add parameters
LOWER_LIMIT: Final[int] = 0
UPPER_LIMIT: Final[int] = 100
random_number: int = random.randint(LOWER_LIMIT, UPPER_LIMIT)


# Easy printing for what the bot says
def bot_message(msg: str) -> None:
    print(f'Bot: {msg}')


# Intro message
bot_message('Welcome to GuessThatNumber™!')
bot_message(f'Guess a number between {LOWER_LIMIT} & {UPPER_LIMIT}.')

# Infinite loop until user guesses
counter: int = 0
while True:
    # Validate user input so it doesn't crash the program
    try:
        user_guess: int = int(input('You: '))
        counter += 1
    except ValueError as e:
        bot_message(f'{e}, please only use numbers.')
        continue

    # Check user input against the number guessed
    if user_guess > random_number:
        bot_message('The number is lower.')
    elif user_guess < random_number:
        bot_message('The number is higher.')
    else:
        bot_message('You guessed correctly! You win!')
        bot_message(f'it took the user {counter} try(ies)')
        break

# Homework:
# 1. Add a score keeping mechanism that includes the amount of tries it took to guess
# the correct number.
