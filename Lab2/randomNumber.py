from random import randint

def randomTestdata(nrOfValues=6,lowest=0,highest=10000):
    array = []
    while nrOfValues >= 0:
        array.append(randint(lowest,highest))
        nrOfValues = nrOfValues -1

    return [randint(lowest, highest), array]


print(randomTestdata())

with open('randomTestFile.txt', 'w') as f:
    N = 0
    while N < 2900:
        f.write(str(randomTestdata())+"\n")
        N += 1