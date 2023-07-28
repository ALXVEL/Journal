import time
from database import add_entry, get_entries, create_table

welcome = '\nWelcome to my Journal!\n'

menu = '\nPlease select one of the following options:\n' \
       '\t1) Add new entry for today.\n' \
       '\t2) View entries.\n' \
       '\t3) Exit.\n' \
       '\nYour selection:'

def prompt_new_entry():
    content = input('What have you learned today? ')
    date = input('Enter the date: ')
    add_entry(content, date)

def view_entries(entries):
    for entry in entries:
        print(f"Content: {entry[0]} \n Date: {entry[1]} \n\n ")

print(welcome)

create_table()

# walrus operator (3.8) while the user_input (which is equal to input(menu) is not 3, it will run the code
while (user_input := input(menu)) != '3':
    time.sleep(1)
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_entries(get_entries())
    else:
        print('\nInvalid option, please try again!')

print('\nExiting...')