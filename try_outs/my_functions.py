def word_sort(txt):
    words = txt.strip().lower().split(' ')
    wlst = list()
    for word in words:
        wtup = (len(word), word)
        wlst.append(wtup)
    wlst.sort()
    wret = list()
    for (length,word) in wlst:
        wret.append(word)
    return wret


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


def count_hours(fhand):
# Return a dictionary with the number of hours received in each time.
    count = dict()
    for line in fhand:
        words = line.strip().split(' ')
        if words and line.startswith('From '):
            hour = words[5].split(':')[0]
            count[hour] = count.get(hour,0) + 1            
    return count


def min_nao_nulo(lst):
    length = len(lst)
    menor = None
    for i in range(length):
        if menor is None or (lst[i] != 0 and menor > lst[i]):
            menor = lst[i]
    return menor


def min_nao_nulo_v2(lst):
    length = len(lst)
    menor = 0
    for i in range(length):
        if menor == 0 or (lst[i] != 0 and menor > lst[i]):
            menor = lst[i]
    return menor


def min_nao_nulo_v3(lst):
    s = None
    for i in lst:
        if s is None or (i != 0 and s > i):
            s = i
    return s