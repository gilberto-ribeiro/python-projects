# Este exercício engloba a reolução do exercício 8.2

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    try:
        print(words[2])
    except:
        continue