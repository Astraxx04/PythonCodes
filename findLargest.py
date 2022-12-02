def findLargest(L):
    s=len(L)
    left=0
    right=s-1
    if s==1:
        return L[0]
    while(left<=right):
        mid=(left+right)//2
        if (mid == s-1):
            nextToMid = 0
        else:
            nextToMid = mid+1

        if (L[mid] > L[nextToMid]):
            return L[mid]
        elif (L[mid] < L[0]):
      # our element is in left of mid
            right = mid-1
        else:
      # our element is in right of mid
            left = mid+1

print(findLargest([8,9,2,3,4,5,6]))