from options import add_contact, all_contacts, edit_contact, find_contact

choice = input("""
     1) Add a contact
     2) Show all contacts
     3) Find a contact
     4) Edit a contact
     
     Enter the number of the option you would like to peform: """)

if choice == '1':
    add_contact()
elif choice == '2':
    all_contacts()
elif choice == '3':
    find_contact()
elif choice == '4':
    edit_contact()
else:
    print("Sorry thats not one of the options")
