string = input('Insert a string: ')
sdict = dict()
for letter in string:

    # sdict[letter] = sdict.get(letter,0) + 1

    if letter in sdict:
        sdict[letter] += 1
    else:
        sdict[letter] = 1

print(sdict)