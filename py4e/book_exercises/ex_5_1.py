count = 0
total = 0
while True:
    inpstr = input('Enter a number: ')
    if inpstr == 'done':
        break
    try:
        value = float(inpstr)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + value
avg = total / count
print(total,count,avg)