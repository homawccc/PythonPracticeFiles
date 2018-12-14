age = int(input("How old are you? "))
height = int(input("How tall are you? "))
weight = int(input("How much do you weigh? "))
#int is required if any math calcs will be used (ex/total below)
# otherwise will just concatenate age, height, weight as strings (5170193)

total = age + height + weight

print(f"So, you're {age} years old, {height} and weigh {weight} pounds = {total}.")