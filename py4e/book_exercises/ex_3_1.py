h = input('Enter Hours: ')
r = input('Enter Rate: ')
try:
    h = float(h)
    r = float(r)
except:
    quit()
if h > 40:
    r = 1.5 * r
p = h * r
print('Pay:',round(p,2))