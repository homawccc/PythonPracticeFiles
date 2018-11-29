my_name = 'Zed A Shaw'
my_age = 35 # not a lie
my_height_in = 73 # inches
my_height_ft  = my_height_in//12
my_height_ft_in = my_height_in - my_height_ft * 12
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print("He's " + str(my_height_in) + " inches tall.") # with '+' operator
print("He's" ,my_height_in, "inches tall.") # with commas
print(f"He's {my_height_in} inches tall.") # f string format
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
print(my_height_ft)
if (my_height_ft_in == 1):
    print(f"I am {my_height_ft} feet {my_height_ft_in} inch tall.")
else:
    print(f"I am {my_height_ft} feet {my_height_ft_in} inches tall.")    

# this line is tricky, try to get it exactly right
total = my_age + my_height_in + my_weight
print(f"If I add {my_age}, {my_height_in}, and {my_weight} I get " + str(total) + ".")
