def Find_Min_Diff(l,p):
    l.sort()
    mindiff=max(l)-min(l)
    n=p
    m=len(l)
    for i in range(m-n+1):
        if l[i+n-1] - l[i] < mindiff:
            mindiff = l[i+n-1] - l[i]
    print(mindiff)
    return mindiff


Find_Min_Diff([3,4,1,9,56,7,9,12],5)
