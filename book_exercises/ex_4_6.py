def computepay(hours,rate):
    if hours > 40:
        rate = 1.5 * rate
    pay = hours * rate
    return pay

def inputfloat(inptext):
    inpstr = input(inptext)
    try:
        inpfloat = float(inpstr)
    except:
        print('Error, please enter numeric input')
        quit()
    return inpfloat

h = inputfloat('Enter Hours: ')
r = inputfloat('Enter Rate: ')
p = computepay(h,r)
print('Pay:',round(p,2))