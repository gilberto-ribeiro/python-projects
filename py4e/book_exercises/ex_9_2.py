fname = input('Enter a file name: ')
try:
    fhand = open(fname,'r')
except:
    print('The file cannot be openned:',fname)
    quit()
count = dict()
for line in fhand:
    line = line.strip()
    words = line.split(' ')
    if len(words) == 0 or words[0] != 'From':
        continue
    try:
        count[words[2]] = count.get(words[2],0) + 1
    except:
        continue
print(count)