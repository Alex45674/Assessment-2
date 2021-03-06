# Imports the options my program offers.
from options import contacts


def Interface():
    # Allows the user to select one of these options.
    choice = input("""
1) Add a contact
2) Show all contacts
3) Find a contact
4) Edit a contact
5) Exit

Enter the number of the option you would like to perform: """)
    print('')

    # Depending on the users input one of the options is ran, if their input isn't valid the program stops.
    if choice == '1':
        contacts.AddContact()
    elif choice == '2':
        contacts.AllContacts()
    elif choice == '3':
        contacts.FindContact()
    elif choice == '4':
        contacts.EditContact()
    elif choice == '5':
        quit()
    else:
        print("Sorry that is not one of the options try again.")

def EditOptions():
    edit = str(input("""
What would you like to do:
1) Change name
2) Change address
3) Change phone number
4) Change birthday
5) Delete the contact

Enter the option you would like to perform: """))
    if edit == '1':
        contacts.ChangeName()
    elif edit == '2':
        contacts.ChangeAddress()
    elif edit == '3':
        contacts.ChangePhonenum()
    elif edit == '4':
        contacts.ChangeBirthday()
    elif edit == '5':
        contacts.Delete()
    else:
        print("Sorry that wasn't an option")
