numbers = []
def createList(listLength):
    i = 0  #needs to be inside function, not otside
    while len(numbers) < listLength:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

createList(8)        

print("The numbers: ")

for num in numbers:
    print(num)