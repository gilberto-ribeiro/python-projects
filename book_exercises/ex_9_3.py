fname = input('Enter file name: ')
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
emails = list(count.keys())
emails.sort()
for email in emails:
    print(email,count[email])
# print(count)