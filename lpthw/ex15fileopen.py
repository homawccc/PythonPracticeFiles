samplefile = open("sampleex15.txt", "a")
samplefile.write("\nThis is an appended line.")
samplefile.close()

samplefile = open("sampleex15.txt", "r")
aline = samplefile.read()
print(aline)
samplefile.close()