# Password Generator

A customizable command-line password generator that lets you choose which types of characters to include.

## What it does

The program asks for the desired password length (must be a positive number) and lets the user choose which character types to include, using a bitmask system similar to Unix `chmod` permissions:

- **1** = Letters (uppercase and lowercase)
- **2** = Numbers
- **4** = Special characters

The values can be added together to combine types. For example:
- `3` (1 + 2) = letters + numbers
- `7` (1 + 2 + 4) = letters + numbers + special characters (default)

If the input is left blank or doesn't match any valid combination, the generator falls back to using all character types.

The program also has a bit of personality — invalid input gets a playful, slightly sarcastic response instead of a plain error message.

## How to run

```bash
python passgen.py
```

## Example usage

```
     Password Generator      
How many characters should the password have? twelve
Are you kidding? Give me a NUMBER
How many characters should the password have? -5
Please, a positive number.
How many characters should the password have? 12

Character types (add up the values to combine):
1 - Letters
2 - Numbers
4 - Special characters
Example: 3 = letters + numbers | 7 = all (default)
Choose (leave blank for default): 3

Your generated password: Xk9pQ2mZ7rTn
```
