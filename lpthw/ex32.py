the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:  #concatenation 1
    print(f"This is count {number}  ", end ="")
print("\n")
for num in the_count:  #concatenation 2
    print("This is count",num)

for i in the_count:  #concatenation 3
    print("This is count " + str(i) + ".")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# NOTICE!! we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in ("shirt"):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
print(elements)    

# now we can print them out too
for i in elements:
    ind = elements.index(i)  #gets the index number of each item in list
    print(f"Element {ind} was: {i}")

elements2 = []
for ii in range(6):
    print(f"Adding {ii} to the list.")
    # append is a function that lists understand
    elements2.append(ii)
print(elements2) 