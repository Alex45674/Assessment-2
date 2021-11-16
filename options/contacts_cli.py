# Imports the options my program offers.
from options import contacts


def interface():
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
        contacts.add_contact()
    elif choice == '2':
        contacts.all_contacts()
    elif choice == '3':
        contacts.find_contact()
    elif choice == '4':
        contacts.edit_contact()
    elif choice == '5':
        quit()
    else:
        print("Sorry that is not one of the options try again.")
