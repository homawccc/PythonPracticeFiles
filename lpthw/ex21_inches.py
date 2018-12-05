#convert height in feet, inches into total inches

def convert(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches

ft = int(input("Enter your height beginning with feet > "))
ins = int(input("Enter your height ending with the inches > ")) 

total = convert(ft, ins)  # var returned representing function result

print(f"You are {total} inches tall.")