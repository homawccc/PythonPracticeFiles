#count words in a string

#counting spaces method
lyric = "The hills are a live with the sound of music"
space = 0
for i in lyric:
    if i == " ":
        space = space + 1
        word = space + 1
print(space)
print(word)

#split by spaces and counting words method
lyric2 = "The hills are alive with the  sound of music"
lyric2_sp = lyric2.split(" ")
words = len(lyric2_sp)
if " " in str(lyric2_sp):
    words = words -1
    lyric2_sp.remove("")
print(lyric2_sp)
print(words)

