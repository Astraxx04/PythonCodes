def sortInRange(L, r):
    countDict = dict.fromkeys(range(r), 0)
    for num in L:
        countDict[num] += 1
    print(countDict)
    index=0
    for key in countDict.keys():
        for i in range(countDict[key]):
            L[index] = key
            index += 1
    print(L)

sortInRange([2,0,1,1,2,3,0,2,1,0,2,3,1,2], 4)