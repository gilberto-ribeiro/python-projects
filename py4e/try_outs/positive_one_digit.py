while True:
    inp = input('Insert an integer:\n')
    if inp == 'Done':
        break
    try:
        n = int(inp)
    except:
        print('It is not an integer, you moron.\n')
        continue
    if n > 0 and n < 10:
        print('It is a positive one digit integer.\n')
    else:
        print('It is not a positive one digit integer.\n')
