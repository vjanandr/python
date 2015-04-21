#!/usr/bin/python3

yrs = int(input("The number of months: "))
rate = float(input("The rate of interest: "))/1200
emi = float(input("The emi you are willing to pay: "))

print("You are eligible to get a loan for {}".
        format((((1+rate)*yrs - 1)*emi)/(rate * (1 + rate)*yrs)))
