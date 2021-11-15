import csv

# executes a section of code that allows the user to add a new contact to the contact data.
def add_contact():

    # Asks the user for the details required to add a new contact.
    name = input("Enter name of the contact being added: ")
    address = input("Enter the address: ")
    phoneno = input("Enter their phone number:")
    birthday = input("Enter their birthday in the form ##/##/####: ")

    # Puts all the new contacts data together to be written as a new row.
    new_contact = (name, address, phoneno, birthday)

    # Opens the contact data file in a way that new data can be written in.
    with open("contact_data.csv","w") as data:
        write_contact = csv.writer(data)

        # Writes the new contacts information in a row.
        write_contact.writerow(new_contact)

def all_contacts():
    # This code print all the contacts stored.
    with open("contact_data.csv","r") as data:
        for line in data:
            print(line)
