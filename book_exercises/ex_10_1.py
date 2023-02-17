def input_file():
# Standard function used to create a file handle to a mbox file.
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname,'r')
    except:
        print('File cannot be openned:',fname)
        quit()
    return fhand


def count_email(fhand):
# Return a dictionary with the number of emails received for each email account.
    count = dict()
    for line in fhand:
        words = line.strip().split(' ')
        if words and line.startswith('From '):
            email = words[1]
            count[email] = count.get(email,0) + 1            
    return count


def sort_dict(dic):
# Sort a dictionary in a reversed order by its values.
    lst = [(val, key) for (key, val) in list(dic.items())]
    lst.sort(reverse=True)
    lst = [(val, key) for (key, val) in lst]
    dic = dict(lst)
    return dic


fhand = input_file()
emails = count_email(fhand)
emails = sort_dict(emails)

lst_emails = list(emails.items())
email, num = lst_emails[0]
print(email,num)