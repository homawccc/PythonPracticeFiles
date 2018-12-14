from sys import argv

script, filename = argv
# .py file and .txt file supplied at initial prompt in Terminal

txt = open(filename)
# variable that represents filename of txt file

print(f"Here's your file {filename}:")

print(txt.read())

txt.close()

file_again = input("Type the filename again: ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()