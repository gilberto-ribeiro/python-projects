def open_file():
    while True:
        fname = input('Insert the name of the file: ')
        if fname == 'done':
            print('\nDone!')
            quit()
        try:
            fhandle = open(fname)
            break
        except:
            print('\n%s cannot be openned.' % fname)
            continue
    return [fhandle,fname]


finfo = open_file()
fh = finfo[0]
fn = finfo[1]

fwrite = open('emails_'+fn,'w')
for line in fh:
    line = line.strip()
    if line.startswith('From:'):
        email = line[6:]
        print(email)
        fwrite.write(email+'\n')
fwrite.close()