l = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
        print('ERROR!')
        continue
    l.append(num)
op = ['Sum:','Count:','Max:','Min:','Avg:']
v = [sum(l),len(l),max(l),min(l),sum(l)/len(l)]
print(l)
for i in range(5):
    print(op[i],v[i])
