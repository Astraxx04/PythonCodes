def binarySearchIndexAndComparisons(L, k):
    s = len(L)
    if(s < 1):
        return (False, 0)
    left = 0
    right = s - 1
    c = 0
    while(left <= right):
        mid = (left + right)//2
        c += 1
        if (k == L[mid]):
            return (True,c)
        elif (k < L[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return(False, c)
    
print(binarySearchIndexAndComparisons([1,2,3,4], 1))