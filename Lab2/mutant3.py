
# Mutant 3
def insertionSortMutant3(array):
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

def memberinArrayMutant3(element, array):
    left = 0
    right = len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left <= right:
        if element < array[x]:
            right = x - 1
        else:
            left = x + 1 
        x = (left + right) // 2

    return (array[x] != element) # (array[x] == element)

def IIIMutant3(element, array):
    sorted = insertionSortMutant3(array)
    print(sorted)
    return memberinArrayMutant3(element, sorted)

print(IIIMutant3(293293, [1, 2, 48, 293293, 909, 3333, 32, 10, 11, 29, 89898, 3, 20]))
