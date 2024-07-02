import os
from cryptography.fernet import Fernet
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "password.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# def write_key():
#     key = Fernet.generate_key()
#     # create and open key.key as key_file- 'wb' special form
#     with open('key.key', 'wb') as key_file:
#         # write in this file key that we generated 
#         key_file.write(key)



def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

master_pwd = input('What is the master password? ')
# add master_pwd encoded to generated key
key = load_key() + master_pwd.encode()
fer = Fernet(key)




def view():
    with open(abs_file_path, 'r') as f:
        # this loop read all lines
        for line in f.readlines():
            # rstrip remove break line
            data = line.rstrip()
            user, passw = data.split('|')
            print('User:', user, '| Password:', fer.decrypt(passw.encode()).decode())
        

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
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')




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

# 1:26:50