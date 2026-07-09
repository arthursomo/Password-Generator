import random
import string

def password_generator():
    print('     Password Generator      ')

    # Validates the length, requiring a positive integer
    while True:
        try:
            length = int(input('How many characters should the password have? '))
            if length > 0:
                break
            print('Please, a positive number.')
        except ValueError:
            print('Are you kidding? Give me a NUMBER')

    print('\nCharacter types (add up the values to combine):')
    print('1 - Letters\n2 - Numbers\n4 - Special characters\nExample: 3 = letters + numbers | 7 = all (default)')

    choice = input('Choose (leave blank for default): ').strip()

    # If nothing is entered, or the input is invalid, use the default (all)
    try:
        choice = int(choice)
    except ValueError:
        choice = 7

    characters = ''
    if choice & 1:
        characters += string.ascii_letters
    if choice & 2:
        characters += string.digits
    if choice & 4:
        characters += string.punctuation

    # If the chosen combination doesn't match any valid option (e.g. 0, 8, 15...), use the default
    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    print(f'\nYour generated password: {password}')

password_generator()
