str = 'X-DSPAM-Confidence:0.8475'
colpos = str.strip().find(':')
number = float(str.strip()[colpos+1:])
print(number)