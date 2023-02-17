while True:
    line = input('> ')
    # if len(line) > 0 and line[0] == '#':
    if line.startswith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')