import os

phone_book_file_name = os.getcwd()+"/"+"phone_book.csv"
phone_book = {}
key_value_seperator = ','

class PhoneBookEntry:
    'Phone book entry details'
    def __init__(self, name, number, address):
        self.name = name;
        self.number = number;
        self.address = address;
    
    def get_details(self):
        return(self.name+key_value_seperator+self.number+key_value_seperator+self.address)

def add_phone_book_entry ():
    details = input("Enter the entry details <name>,<number>,<address> :")

    entry = details.split(',')
    if entry[0] in phone_book:     
        if not input("There is already an entry for this name overwrite [Yes/y] ? :").islower() == 'y':
            print("{} ignored".format(entry[0]))
            return

    if not entry[1].isdigit():
        raise Exception("Invalid input: Phone number should be an integer.") 
      
    phoneObj = PhoneBookEntry(entry[0],entry[1],entry[2])
    phone_book[entry[0]] = phoneObj
    print(phone_book)
    
def lookup_phone_book_entry ():
    name = input("Enter the name of the person :")
    if name in phone_book:
        print("The details of {} are {}".format(name, phone_book[name].get_details()))
    else:
        print("There is no entry for {}".format(name))    
    

def update_phone_book ():
    phone_book_file  = open(phone_book_file_name, 'a')
    phone_book_file.seek(0)
    phone_book_file.truncate()
    
    for entry in phone_book:
        val = phone_book[entry]
        phone_book_file.writelines("{name}{seperator}{number}{seperator}{address}\n".
                                   format(name=entry, seperator=key_value_seperator, 
                                   number = val[0], address = val[1]))
    phone_book_file.close()

def load_phone_book ():
    with open(phone_book_file_name, 'r') as phone_book_file:
        for line in phone_book_file:
            key_value = line.split(key_value_seperator)
            phoneObj = PhoneBookEntry(key_value[0],key_value[1],key_value[2].rstrip())
            phone_book[key_value[0]] = phoneObj
            
def handle_input (in_val):
    try:
        if (in_val == 1):
            add_phone_book_entry() 
             
        if (in_val == 2):
            lookup_phone_book_entry()
        
        if (in_val == 3):
            update_phone_book()
            quit()
    except Exception as e:
        raise e        
 
if __name__ == '__main__':
    print("Welcome to the phone book utility")
    load_phone_book()
    while True:
        try:
            print("Choose an action:")
            print("1: Add a phone book entry")
            print("2: Lookup a phone book entry")
            print("3: Exit")
            in_val = int(input(":>> "))
            handle_input(in_val)
        except Exception as e:
            print(e)
        