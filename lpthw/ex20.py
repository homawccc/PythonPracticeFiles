from sys import argv

script, input_file = argv

f = input_file
#added by me

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

#line_count and f are args that represent the line count and file    

current_file = open(f)
#current_file variable now represents file name sent in opening arg
# me - it originally used open(input_file) instead of f

print("First let's print the whole file:\n")
#prints all lines from arg file (test.txt)
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#sends cursor back to beginning of file 
rewind(current_file)

print("Let's print three lines:")

#creates a line counter beginning at 1
current_line = 1

#prints line count (1) and 1st line from file
print_a_line(current_line, current_file)

#adds 1 to current line count
current_line = current_line + 1

#prints line count (2) and 2nd line from file
print_a_line(current_line, current_file)

#adds 1 to current line count
current_line = current_line + 1

#prints line count (2) and 2nd line from file
print_a_line(current_line, current_file)