
# Mutant 1
def insertionSortmutant1(array):
    maxSwap = len(array)
    i = 1
    while i < maxSwap:
        j = i
        while (j > 0) and (array[j] < array[(j - 1)]):
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp
            j = j - 1 
        i = i + 1
    return array

def memberinArraymutant1(element, array):
    left = 0
    right = len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left > right: # > is not <= 
        if element < array[x]:
            right = x - 1
        else:
            left = x + 1
        x = (left + right) // 2

    return (array[x] == element)

def IIImutant1(element, array):
    sorted = insertionSortmutant1(array)
    print(sorted)
    return memberinArraymutant1(element, sorted)

print(IIImutant1(3, [1, 2, 48, 293293, 909, 3333, 32, 10, 11, 29, 89898, 3, 20]))
