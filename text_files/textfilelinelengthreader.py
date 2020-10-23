x = open('Data.txt', 'r')

for y in x:
    y = y.split(',')
    y[-1] = y[-1].strip()
    print(y[0] ,len(y))