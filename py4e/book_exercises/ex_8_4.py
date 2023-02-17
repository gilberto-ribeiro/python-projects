fhand = open('romeo.txt')
unique_words = list()
for line in fhand:
    try:
        words = line.strip().split(' ')
    except:
        continue
    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)
unique_words.sort()
print(unique_words)