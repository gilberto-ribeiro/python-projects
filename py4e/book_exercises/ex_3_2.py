h = input('Enter Hours: ')
try:
    h = float(h)
except:
    print('Error, please enter numeric input')
    quit()
r = input('Enter Rate: ')
try:
    r = float(r)
except:
    print('Error, please enter numeric input')
    quit()
if h > 40:
    r = 1.5 * r
p = h * r
print('Pay:',round(p,2))