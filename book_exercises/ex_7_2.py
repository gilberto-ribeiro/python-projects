fname = input('Enter the file name: ')
try:
    fhandle = open(fname,'r')
except:
    print('Invalid file name.')
    exit()
total = 0
count = 0
for line in fhandle:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        value = float(line[-6:])
        count = count + 1
        total = total + value
avg = total / count
print('Average spam confidence:',avg)