#Asks the user for the details required to add a new contact.
name = input("Enter name of the contact being added: ")
address = input("Enter the address: ")
phoneNo = input("Enter their phone number:")
birthday = input("Enter their birthday in the form ##/##/####: ")

with open("contact_data.csv","w") as data:
    data.write(name,address,phoneNo,birthday)
