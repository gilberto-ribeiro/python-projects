def count_start(fhandle,text):
    count = 0
    for line in fhandle:
        if line.startswith(text):
            count = count + 1
    return count


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
c = count_start(finfo[0],'Subject:')
print('\nThere were %d subject lines in %s.' % (c,finfo[1]))