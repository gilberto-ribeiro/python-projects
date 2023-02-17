def count(string,letter):
    inc = 0
    for word in string:
        if word == letter:
            inc = inc + 1
    return inc

s = input('Enter a string: ')
l = input('Enter a letter: ')
print(count(s,l))