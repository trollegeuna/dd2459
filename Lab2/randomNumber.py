from random import randint

def randomTestdata(nrOfValues=20,lowest=0,highest=10000):
    array = []
    while nrOfValues >= 0:
        array.append(randint(lowest,highest))
        nrOfValues = nrOfValues -1

    return array


print(randomTestdata())