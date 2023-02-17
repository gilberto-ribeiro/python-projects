def adv(n):
    import random
    x = []
    for i in range(n):
        x.append(random.randint(1,20))
    return [min(x), max(x), x]


print(type(adv))
print(adv)


while True:
    inp = input('Insira do número de d20: ')
    inp = int(inp)
    print(adv(inp))

