phone_book = {}

def add_phone_book_entry ():
    name = input("Enter the name of the person :")   
    if name in phone_book:     
        if not input("There is already an entry for this name overwrite [Yes/y] ? :").islower() == 'y':
            print("Input {} ignored".format(name))
            return

    number = input("Enter the phone number :")
            
    phone_book[name] = number

    print(phone_book)
    
def lookup_phone_book_entry ():
    name = input("Enter the name of the person :")
    if name in phone_book:
        print("The phone number of {} is {}".format(name, phone_book[name]))
    else:
        print("There is no entry for {}".format(name))    
    
def handleInput (in_val):
    if (in_val == 1):
        add_phone_book_entry()
    
    if (in_val == 2):
        lookup_phone_book_entry()
    
    if (in_val == 3):
        quit()
    
if __name__ == '__main__':
    print("Welcome to the phone book utility")
    while True:
        print("Choose an action:")
        print("1: Add a phone book entry")
        print("2: Lookup a phone book entry")
        print("3: Exit")
        in_val = int(input(":>> "))
        handleInput(in_val)
        