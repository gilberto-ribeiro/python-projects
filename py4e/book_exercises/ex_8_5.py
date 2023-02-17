fname = input('Enter a file name: ')
try:
    fhand = open(fname,'r')
except:
    quit()
emails_received = list()
for line in fhand:
    words = line.strip().split()
    if len(words) == 0 or words[0] != 'From':
        continue
    emails_received.append(words[1])
for email in emails_received:
    print(email)
print('There were',len(emails_received),'lines in the file with From as the first word')