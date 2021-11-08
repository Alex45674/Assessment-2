#This code print all the contacts stored.
with open("contact_data.csv","r") as data:
    for line in data:
        print(line)
