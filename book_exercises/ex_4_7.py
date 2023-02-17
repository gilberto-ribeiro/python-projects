def computegrade(score):
    if score < 0 or score > 1:
        grade = 'Bad score'
    else:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
    return grade

inp = input('Enter score: ')
try:
    x = float(inp)
except:
    print('Bad score')
    quit()
print(computegrade(x))