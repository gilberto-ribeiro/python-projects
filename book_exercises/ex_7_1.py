fname = input('Enter a file name: ')
fhandle = open(fname,'r')
for line in fhandle:
    print(line.rstrip().upper())