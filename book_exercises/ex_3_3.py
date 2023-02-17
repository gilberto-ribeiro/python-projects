inp = input('Enter score: ')
try:
    x = float(inp)
except:
    print('Bad score')
    quit()
if x < 0 or x > 1:
    print('Bad score')
else:
    if x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    else:
        print('F')