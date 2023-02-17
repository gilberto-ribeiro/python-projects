count = 0
total = 0
smallest = None
largest = None
while True:
    inpstr = input('Enter a number: ')
    if inpstr == 'done':
        break
    try:
        value = float(inpstr)
    except:
        print('Invalid input')
        continue
    # count = count + 1
    # total = total + value
    if smallest is None or smallest > value:
        smallest = value
    if largest is None or largest < value:
        largest = value
# avg = total / count
# print(total,count,avg)
print(smallest,largest)