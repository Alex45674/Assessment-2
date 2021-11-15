
def add_contact():
    # Asks the user for the details required to add a new contact.
    name = input("Enter name of the contact being added: ")
    address = input("Enter the address: ")
    phoneno = input("Enter their phone number:")
    birthday = input("Enter their birthday in the form ##/##/####: ")

    with open("contact_data.csv","w") as data:
        data.write(name,address,phoneno,birthday)

def all_contacts():
    # This code print all the contacts stored.
    with open("contact_data.csv","r") as data:
        for line in data:
            print(line)
