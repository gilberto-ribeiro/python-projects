while True:
    n = input('Insert a number:\n')
    if n == 'Done':
        break
    n = int(n)
    if n%2 == 0:
        print('It is an even number')
    else:
        print('It is an odd number')