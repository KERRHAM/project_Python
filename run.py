import random

# Variable for declaring maximum lines to chose from (3)
MAX_LINES = 3
# Variable for declaring Maximum value for a user to deposit(100)
MAX_VALUE = 100
# Variable for decalaring Minimum value for a user to deposit(1)
MIN_VALUE = 1
# Variable for number of rows in game (3)
rows = 3
# Variable for number of columns in game (3)
cols = 3

# Dicitionary for number of symbols to generate
# 2 A's, 4 B's, 6 C's & 8 D's
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Dictionary for storing Value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function for checking the rows for a sequence of 3 of the same symbols and
# adding the number of winning lines to a list and calculating winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)


    return winnings, winning_lines

# Function for generating random rows/columns of symbols
def spin_vending_machine(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function for displaying game board
# Empty print() used to start newline after board is displayed for vertical spacing
def display_vending_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

# Function for Depositing funds from the user to play the game and
# for checking deposit entered is > 0 and is a number(Integer)
def deposit():
    print(
        '''
        Welcome user are you ready to play the Bottle cap vending machine?
        To play deposit a bottlecap to win yourself some tokens to exchange
        for any supplies needed!!

        Minimum deposit is 1 and maximum is 100, a table will display with 
        3 lines and you Must have 3 Matching symbols horizontally to win.
       
        The Vending machine has 3 lines with 4 Symbols available, A B C D
        Value A will Multiply your deposit by 5
        Value B will Multiply your deposit by 4
        Value C will Multiply your deposit by 3
        Value D will Multiply your deposit by 2
        
        '''
    )


    while True:
        amount = input("How many Bottlecaps would you like to deposit?\n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= 100:
                break
            else:
                print("Deposit must be between 1 and 100!!")
        else:
            print("Please enter a number.")

    return amount
