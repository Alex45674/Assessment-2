import csv
from options import contacts_cli
# Executes a section of code that allows the user to add a new contact to the contact data.
def add_contact():

    print("You have selected option 1 (Add a contact):")
    print('')

# Asks the user for the details required to add a new contact.
    name = input("Enter the full name (first and last names) of the contact being added: ")
    address = input("Enter their street address: ")
    phoneno = input(str("Enter their phone number: "))
    birthday = input("Enter their birthday in the form ##/##/####: ")

# Puts all the new contacts data together to be written as a new row.
    new_contact = (name, address, phoneno, birthday)

# Opens the contact data file in a way that new data can be added onto the end of the contact data file.
    with open("contact_data.csv", "a", newline='') as data:
        write_contact = csv.writer(data)

# Writes the new contacts information in a row.
        write_contact.writerow(new_contact)
    print('')
    print("New contact added.")

# Executes a section of code that allows the user to view all contacts stored in the contacts data file.
def all_contacts():

    print("You have selected option 2 (Show all contacts):")
    print('')

# This opens the contact data for reading
    with open("contact_data.csv", "r") as data:
        # This print each line in the csv file
        for line in data:
            print(line)

    print("All contacts shown.")

# Executes a section of code that allows the user to find a contact by entering a name,address,phone number or birthday.
def find_contact():

    print("You have selected option 3 (Find a contact):")
    print('')
# Creates an empty list to store the contacts information.
    contacts_list = []
# Opens the file contact data
    with open("contact_data.csv", newline = '') as data:
        read_data = csv.reader(data, delimiter = ',')
# For each row in contact data, it is added on to the end of my list (contact_list)
        for row in read_data:
            contacts_list.append(row)

# Asks the user to enter one bit of information about the contact their trying to find.
    search_info = str(input("""Enter the full name (first and Last), street address, phone number or birthday of the
contact you want to find. (Note when entering a birthday please enter it in the form ##/##/####): """))
    print('')
# This is used to keep track of what row the information is located.
    row_num = -1
# This is used to check a contacts exists.
    check = False
# Goes through each row in my contacts_list.
    for row in contacts_list:
# Adds one to the row number to show it's starting to search a new row.
        row_num = row_num + 1
        for information in row:
# Checks if any of the contact information in that row is the same as the inputted search information.
            if information == search_info:
                print("Contact(s) found: ", contacts_list[row_num])
# Check is set to true to we know the contact exists.
                check = True
# If the desired information isn;t found and the loop has gone through all rows this code will be ran.
            else:
# Allows the loop to continue
                continue
# Runs if contact doesn't exist.
    if check == False:
        print('Contact does not exist.')

def edit_contact():

    print('You have selected option 4 (edit a contact)')
    print('')

# Again creates an empty list.
    contacts_list = []

# Opens the file contact data.
    with open("contact_data.csv", newline = '') as data:
        read_data = csv.reader(data, delimiter = ',')

# For each row in contact data, it is added on to the end of my list (contact_list).
        for row in read_data:
            contacts_list.append(row)

# Asks the user to enter one bit of information of the contact their trying to edit so the contact can be located.
    search_info = str(input("""Enter the full name (first and Last), street address, phone number or birthday of the
contact you want to edit. (Note when entering a birthday please enter it in the form ##/##/####): """))

# This is used to keep track of what row the information wanting to be edited is located.
    row_num = -1
# This is used to check a contacts existence.
    check = False
# Goes through each row in my contacts_list.
    for row in contacts_list:
# Adds one to the row number to show it's starting to search a new row.
        row_num = row_num + 1
        for information in row:
# Checks if any of the contact infromation in that row is the same as the inputted search information.
            if information == search_info:
                print('')
# Shows the user the first contact to be found.
                print("Contact(s) found: ", contacts_list[row_num])
# Check is set to true so we know the contact exists.
                check = True
# Asks the user if this is the correct contact.
                search = str(input("""
Is this the contact you wanted to edit?
Please enter 'yes' if it is or 'no' to keep searching: """))
# Depending on the users input
                if search == 'yes':
                    contacts_cli.edit_options()
                    break
                elif search == 'no':
                    check = False
                    break
            else:
# Allows the loop to continue.
                continue
# Runs if the contact doesn't exist.
    if check == False:
        print('')
        print('Contact does not exist.')


def change_name():
    print('')
    new_name = str(input('Please enter the new full name (first and last names): '))

def change_address():

def change_phonenum():

def change_birthday():

def delete():
