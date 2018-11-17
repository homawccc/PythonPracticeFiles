print("Hello World")
print(type (True))
x = input("Please enter a number:")
x=int(x)
y = input("Please enter a another number:")
y=int(y)
z = input("Please enter a third number:")
z =int(z)

if (x%2!=0 and x>y and x>z):
    if (y%2!=0 or z%2!=0):
        print(str(x)+" is the largest odd number.")
elif (y%2!=0 and y>x and y>z):
    if (y%2!=0 or z%2!=0):
        print(str(y)+" is the largest odd number.")
elif (z%2!=0 and z>x and z>y):
    if (x%2!=0 or z%2!=0):
        print(str(z)+" is the largest odd number.")
else:
    print("There are no odd numbers")
#Comment added in GutHub Editor    
