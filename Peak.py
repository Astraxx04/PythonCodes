def peak_unimodal(A):
    low = 0
    high = len(A)-1
    while True:
        mid = (low+high)//2
        if A[mid-1]<A[mid] and A[mid]<A[mid+1]:
            low = mid
        elif A[mid-1]>A[mid] and A[mid]>A[mid+1]:
            high = mid
        else:
            return mid
L=[2, 3, 4, 21, 43, 52, 51, 18, 11, 9, 6, 5, 1]
res = peak_unimodal(L)
print(res)