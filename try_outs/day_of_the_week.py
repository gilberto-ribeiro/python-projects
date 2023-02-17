fhandle = open('mbox-short.txt')
dayweek = list()
for line in fhandle:
    line = line.strip()
    if line.startswith('From '):
        part = line.split(' ')
        dayweek.append(part[2])
for i in dayweek:
    print(i)
