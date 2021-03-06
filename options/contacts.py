import csv
from options import contacts_cli

# creates an empty list.
contacts_list = []

# Opens the file contact data.
with open("contact_data.csv", newline = '') as data:
    read_data = csv.reader(data, delimiter = ',')

# For each row in contact data, it is added on to the end of my list (contact_list).
    for row in read_data:
        contacts_list.append(row)

temp_row = 0

def AddContact():

# Tested if a contact was added through my interface. No further testing needed.
    print("You have selected option 1 (Add a contact):")
    print('')

# Asks the user for the details required to add a new contact.
    name = str(input("Enter the full name (first and last names) of the contact being added: "))
    address = str(input("Enter their street address: "))
    phoneno = str(input("Enter their phone number: "))
    birthday = str(input("Enter their birthday in the form ##/##/####: "))

# Puts all the new contacts data together to be written as a new row.
    new_contact = [name, address, phoneno, birthday]

    contacts_list.append(new_contact)
    print('')
    print("New contact added.")

# Executes a section of code that allows the user to view all contacts stored in the contacts data file.
def AllContacts():
# Tested if all contacts are shown through my interface. No further testing needed.
    print("You have selected option 2 (Show all contacts):")
    print('')
    print(contacts_list)
    print('')
    print("All contacts shown.")

# Executes a section of code that allows the user to find a contact by entering a name,address,phone number or birthday.
def FindContact():
# Tested if a contact can be found using my interface, if there are multiple contacts it asks the user if the one shown
# first is their desired contact if not it shows the next contact that matched with their search data.
# If they input any data that doesn't match any contact data they are told the contact does not exist.
    print("You have selected option 3 (Find a contact):")
    print('')

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
                print("Contact found: ", contacts_list[row_num])
# Check is set to true to we know the contact exists.
                check = True
# If the desired information isn;t found and the loop has gone through all rows this code will be ran.
            else:
# Allows the loop to continue
                continue
# Runs if contact doesn't exist.
    if check == False:
        print('Contact does not exist.')

def EditContact():
# Tested if a contacts can be found same as my find_contact function, also tested if they input an option that does not
# exist and how my program handles it. Finally tested if my programm successfully edits the desired contact and updates
# the list containing all contacts.
    print('You have selected option 4 (edit a contact)')
    print('')

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
                print("Contact found: ", contacts_list[row_num])
# Check is set to true so we know the contact exists.
                check = True
# Asks the user if this is the correct contact.
                search = str(input("""
Is this the contact you wanted to edit?
Please enter 'yes' if it is or 'no' to keep searching: """))
# Depending on the users input.
                if search == 'yes':
                    global temp_row
                    temp_row = row_num
                    contacts_cli.EditOptions()
                    return
                elif search == 'no':
                    check = False
                    continue
                else:
                    print('Not an option')
                    return
# Runs if the contact doesn't exist.
    if check == False:
        print('')
        print('Contact does not exist.')


def ChangeName():
    print('')
# Asks the user to input the new name.
    new_name = str(input('Please enter the new full name (first and last names): '))
# Replaces the old name of the users desired contact with their new one.
    contacts_list[temp_row][0] = new_name
    print('')
    print("Contact updated: ", contacts_list[temp_row])

def ChangeAddress():
    print('')
# Asks the user to input the new street address.
    new_address = str(input('Please enter the new street address: '))
# Replaces the old street address of the users desired contact with their new one.
    contacts_list[temp_row][1] = new_address
    print('')
    print("Contact Updated: ", contacts_list[temp_row])

#
def ChangePhonenum():
    print('')
# Asks the user to input the new phone number.
    new_phonenum = str(input('Please enter the new phone number: '))
# Replaces the old phone number of the users desired contact with their new one.
    contacts_list[temp_row][2] = new_phonenum
    print('')
    print("Contact updated: ", contacts_list[temp_row])

def ChangeBirthday():
    print('')
# Asks the user to input the new birthday date.
    new_birthday = str(input('Please enter the new birthday date in the form ##/##/####: '))
# Replaces the old birthday date of the users desired contact with their new one.
    contacts_list[temp_row][3] = new_birthday
    print('')
    print("Contact updated: ", contacts_list[temp_row])

def Delete():
    # Deletes the contact from the list.
    contacts_list.pop(temp_row)
    print('')
    print('Contact deleted')
