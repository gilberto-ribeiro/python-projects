from my_functions import input_file


def count_hours(fhand):
# Return a dictionary with the number of hours received in each time.
    count = dict()
    for line in fhand:
        words = line.strip().split(' ')
        if words and line.startswith('From '):
            if '' in words:
                words.remove('')
            hour = words[5].split(':')[0]
            count[hour] = count.get(hour,0) + 1            
    return count


def sort_by_key(dic):
# Return a dictionary sorted by its key.
    lst = list(dic.items())
    lst.sort()
    dic = dict(lst)
    return dic


fhand = input_file()
hours = count_hours(fhand)
hours = sort_by_key(hours)

for hour in hours:
    print(hour,hours[hour])