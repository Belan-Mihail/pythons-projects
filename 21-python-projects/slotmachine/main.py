
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