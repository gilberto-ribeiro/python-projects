import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname,'r')
except:
    print('File cannot be openned:',fname)
    quit()

count = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower().strip()
    words = line.split(' ')
    for word in words:
        count[word] = count.get(word,0) + 1
fout = open('contagem_de_palavras','w')
keys = list(count.keys())
keys.sort()
for key in keys:
    roll = key+' '+str(count[key])+'\n'
    fout.write(roll)
fout.close()