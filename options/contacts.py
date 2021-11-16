import csv
# Executes a section of code that allows the user to add a new contact to the contact data.
def add_contact():

    print("You have selected option 1 (Add a contact)")
    print('')

    # Asks the user for the details required to add a new contact.
    name = input("Enter name of the contact being added: ")
    address = input("Enter the address: ")
    phoneno = input(str("Enter their phone number in the form: "))
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

    print("You have selected option 2 (Show all contacts)")
    print('')

    # This opens the contact data for reading
    with open("contact_data.csv", "r") as data:
        # This print each line in the csv file
        for line in data:
            print(line)

    print('')
    print("All contacts shown.")

# Executes a section of code that allows the user to find a contact by entering a name,address,phone number or birthday.
def find_contact():

    print("You have selected option 3 (Find a contact)")
    print('')
    # Creates an empty list to store the contacts information
    contacts_list = []
    # Opens the file contact data
    with open("contact_data.csv", newline='') as data:
        read_data = csv.reader(data, delimiter = ',')
        # For each row in contact data it is added on to the end of my list (contact_list)
        for row in read_data:
            contacts_list.append(row)

        # Asks the user to enter one of the
        search_info = str(input("""Enter the name, address, phone number or birthday of the contact you want to find
(Note when entering a birthday please enter it in the form ##/##/####): """))

        row_num = 0
        # Goes through each row in my contacts_list
        for row in contacts_list:
            for information in row:
                row_num = row_num + 1
                if information == search_info:
                    print("Contact found: ", contacts_list[row_num])
                    break
                else:
                    continue

