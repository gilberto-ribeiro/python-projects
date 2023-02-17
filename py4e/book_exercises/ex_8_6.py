numbers = list()
while True:
    inpstr = input('Enter a number: ')
    if inpstr == 'done':
        break
    try:
        inpfloat = float(inpstr)
    except:
        continue
    numbers.append(inpfloat)
print('Maximum:',max(numbers))
print('Minimum:',min(numbers))