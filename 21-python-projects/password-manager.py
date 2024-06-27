import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "password.txt"
abs_file_path = os.path.join(script_dir, rel_path)

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
    # '\n' line break
    with open(abs_file_path, 'a') as f:
        f.write(name + '|' + pwd + '\n')




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