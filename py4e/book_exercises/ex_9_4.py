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
        count[words[1]] = count.get(words[1],0) + 1
    except:
        continue
largest = None
for key in count:
    if largest is None or count[largest] < count[key]:
        largest = key
print(largest,count[largest])