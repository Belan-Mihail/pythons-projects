master_pwd = input('What is the master password? ')

def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input('Account Password: ')
 
    # automatically close this file
    # a mode allow us to add data to the end if file exist or create new file
    # r mode allow us only read file
    # w mode overwrite (clear and create new one) all data if file already exist
    # f it is name off our file 
    with open('password.txt', 'a') as f:
        f.write(name + '|' + pwd)




while True:
    mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else: 
        print('Invalid mode')
        continue