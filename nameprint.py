#!/usr/bin/python3

name = input("Enter you name: ")
age_in_str = input("Enter your age: ")

#age_in = int(age_in_str)
age_in = age_in_str.digits()

if age_in >= 65:
    print("Hello {} you are never too old to learn python at"
            " {}".format(name, age_in))
elif age_in < 65 and age_in >= 30:
    print("Hello {} how did you get by for {} years without "
            "python!".format(name, age_in))
else:
    print("Hello {} today is a great day to learn python".format(name))
