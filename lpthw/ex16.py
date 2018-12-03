f = open("test1.txt", "w")
f.write("This is some content\n")
f.write("This is some additional content\n")
f.close()

with open("test1.txt", "r") as rf:
    with open("text2.txt", "w") as wf:
        for line in rf:
            wf.write(line)