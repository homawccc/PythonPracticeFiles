def count(text, aChar):
    lettercount = 0
    for i in text:
        if i == aChar:
            lettercount = lettercount + 1
    return lettercount

print(count("banana","a"))

#Hello from Git