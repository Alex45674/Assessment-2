import csv
# executes a section of code that allows the user to add a new contact to the contact data.
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

def all_contacts():

    print("You have selected option 2 (Show all contacts)")
    print('')

    # This code print all the contacts stored.
    with open("contact_data.csv", "r") as data:
        for line in data:
            print(line)

    print('')
    print("All contacts shown.")
