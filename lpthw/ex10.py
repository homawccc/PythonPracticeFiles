tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." # escapes a backslash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

songquote = "\"Some girls are bigger than others...\""
authorquote = "\n\t-by The Smiths"

print("I like the lyric:\n",songquote, authorquote)

fcars = ["Saab", "Volvo", "BMW", "Honda", "Toyota"]
dcars = ["Chevy", "Ford", "Jeep", "Chysler", "Dodge"]
cars = [fcars, dcars]

# fcars.insert(0, "Hyundai") this adds it to beginining
fcars.append("Hyundai") # appends to end of list
# del fcars[3] removes item from list by element number
# fcars.remove("Toyota") removes item by value
print(cars)
print(len(fcars))
