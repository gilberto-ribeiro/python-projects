fhand = open('words.txt','r')
wdict = dict()
for line in fhand:
    words = line.strip().split()
    for word in words:
        word = word.lower()
        if word in wdict:
            continue
        wdict[word] = word.upper()
print(wdict)