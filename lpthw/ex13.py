from sys import argv

first = input("Type your first name: ")
last = input("Type your last name: ")
month = input("Type your birth month: ")
day = input("Type day of month of birthday: ")

script = argv

print("The script is called:", script)
print("Your first name is:", first)
print("Your last name is:", last)
print("You were born oin:", month)
print("You were born on this day:", day) # replaces argv with input value
# when run from command line supplying 4 args