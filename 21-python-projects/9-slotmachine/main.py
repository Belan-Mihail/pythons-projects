import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # chec every line
    for line in range(lines):
        # first symbol or row- we want to check if this symbol the same symbols in another columns
        symbol = columns[0][line]
        for column in columns:
            # check line
            symbol_to_check = column[line]
            # if symbols != another symbol = break user is lose
            if symbol != symbol_to_check:
                break
            # if the symbols same_ user win
        else: 
            winnings += values[symbol] * bet * 3
            winning_lines.append(line + 1)
    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .tems give us a key and associated value for this key
    for symbol, symbol_count in symbols.items():
        # loop repeat symbol_accont value times for each key
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    # generate a column
    for _ in range(cols):
        column = []
        # [:] - slice meth to copy list all_symbols in list current_symbols
        current_symbols = all_symbols[:]
        # generate rows
        for _ in range(rows):
            value = random.choice(current_symbols)
            # we remove value from current_symbol. so that value is not repeated more than allow number times 
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    # loop durch every single row
    for row in range(len(columns[0])):
        # loop every colum
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()





def deposit():
    while True:
        amount = input('What you would like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Invalid value')
    
    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter correct number of lines')
        else:
            print('Invalid value')
    
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():

            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}  ')
        else:
            print('Invalid value')
    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f'Your are betting ${bet} on ${lines} lines- Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'you won ${winnings}')
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    

main()