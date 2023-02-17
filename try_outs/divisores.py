x = input('Insira um número:\n')
x = int(x)
for i in range(x+1):
    if i == 0:
        continue
    r = x%i
    if r == 0:
        print(i)
print('The End!')