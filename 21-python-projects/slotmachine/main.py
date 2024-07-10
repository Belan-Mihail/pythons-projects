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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .tems give us a key and associated value for this key
    for symbol, symbol_count in symbols.items():
        # loop repeat symbol_accont value times for each key
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [[], [], []]
    for col in range(cols):
        column = []
        # [:] - slice meth to copy list all_symbols in list current_symbols
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            # we remove value from current_symbol. so that value is not repeated more than allow number times 
            current_symbols.remove(value)




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
        bet = input(f'Enter your bet. Amount must be between ${MIN_BET} - ${MAX_BET}  ')
        if bet.isdigit():

            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}  ')
        else:
            print('Invalid value')


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f'Your are betting ${bet} on ${lines} lines- Total bet is equal to: ${total_bet}')


main()