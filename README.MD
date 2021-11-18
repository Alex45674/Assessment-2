CSC1034: Assessment 2
=====================
Here is my simple contact application for CSC1034 Assessment 2. This program accesses a csv file that contains a few 
sample contacts. The program opens and reads this file and adds them to a separate list within my code. Using this list
users can add a contact too it, get it to display all contacts present in the list, find a specific contact within the
list of contacts as well as edit any contact that is present in the list. Editing the contact means the user can change
a contacts name, address, phone number and birthday. They are also able to delete a contact from the list entirely.

You are able use my program by running the main.py file. From there you are able to navigate through my contacts 
program. I have not included a separate testing file as I feel you are able to test my program through the command line
interface which is how I tested my own program but I was not sure on how to show this.

When opening my csv file to check if the data is stored there please open the file in note pad, not excel as excel
destoys the leading zeros for the phone numbers.

Assumptions made whilst making this program:
--------------------------------------------

1. When adding a new contact, I have assumed the user will:
    
    i) Input the first and last name, with capitals, when asked to input the name of the new contact.
    
    ii) Input only the street address (eg 67 Springfield Road) with numbers and capitals where appropriate when asked 
    to input the new contacts street address.
    
    iii) Input only numbers with no white spaces when asked to input the new contacts phone number.
    
    iv) Input a birth date in the form: ##/##/#### (including the slashes) where the '#' are numbers when asked to
    input the new contacts birth date.
    
2.  When finding a specific contact, I have assumed users will:

    i) Input the first and last name, with capitals, when using a name to search for a contact to find it.
    
    ii) Input only the street address (eg 67 Springfield Road) with numbers and capitals where appropriate when using 
    the street address to search for a contact to find it.
    
    iii) Input numbers only, with no white spaces, when using a phone number to search for a contact.
    
    iv) Input a birthday date in the form: ##/##/#### (including the slashes) where the '#' are numbers when using a
     birth date to search for a contact to find it.
     
     If these assumptions are not met my code will simply tell the user the contact their looking for does not exist.

3. When editing a contact, I have assumed the users will:
    
    i) The user will input one piece of information (either the name, address, phone number or birthday) exactly how it 
    is written within the contact data to find it. So, for name it would have to be spelt the same with capitals and 
    spaces in the exact same place, the same would go for street address with the number and street name in the same 
    order, spelt the same with capitals in the same places. For phone numbers they would input only numbers with no 
    white spaces and for birth date it would have to be inputted in the form: ##/##/####.
    
    ii) When asked to input the data they want to change the contact data to, they must also follow the same assumptions
    for the name, address, phone number and birthday as all my other assumptions stated previously.

    If these assumptions are not met my code will again simply say the contact that their looking for does not exist
