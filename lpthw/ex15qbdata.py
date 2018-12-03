infile = open("qbdata.txt", "r")
line = infile.readline()
ratings_list = []
#while line:
for i in range(4): #runs 4 times (lines)
    values = line.split() 
    #creates a list from each line called "values"
    print('QB ', values[0], values[1], 'had a rating of', float(values[10]) )
    #combines strings and values frm the list
    ratings_list.append(values[10])
    line = infile.readline()
    #reassigns line variable to next line to avoid infinite loop
    
infile.close()
ratings_list.sort()
print(ratings_list)