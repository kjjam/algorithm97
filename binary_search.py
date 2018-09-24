def binarySearch(array, startIndx, endIndx, target):
    if endIndx >= startIndx :
        mid = startIndx + (endIndx - startIndx) / 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            return binarySearch(array, startIndx, mid - 1, target)
        else:
            return binarySearch(array, mid + 1, endIndx, target)
    else: return -1

def test():
    testList=[1,3,7,9,10,13]
    for item in testList:
        print binarySearch(testList,0, len(testList)-1, item )

test()