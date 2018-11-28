tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

songquote = "\"Some girls are bigger than others...\""
authorquote = "\n\t-by The Smiths"

print ("%s %s %s" % ("I like the lyric: ", songquote, authorquote))

fcars = ["Saab", "Volvo", "BMW", "Honda", "Toyota"]
dcars = ["Chevy", "Ford", "Jeep", "Chysler", "Dodge"]
cars = [fcars, dcars]

fcars.append("Hyndai")
print (cars)
print (len(fcars))
