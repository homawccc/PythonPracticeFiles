numbers = []
def createList(listLength):
    i = 0  # needs to be inside function, not otside
    inc = 2 # variable representing incrementing value
    for i in range(0,listLength):
        print(f"At the top i is {i}")
        numbers.append(i)

        #i = i + inc  (ignored in this version until end of loop)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

createList(10)        

print("The numbers: ")

for num in numbers:
    print(num)