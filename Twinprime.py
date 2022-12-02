def prime(x):
    if(x<2):
        return False
    for i in range(2,x//2+1):
        if(x%i==0):
            return False
    return True
    
def Twinprime(a,b):
    res=[]
    for i in range(a,b-1):
        if(prime(i)==True):
            if(prime(i+2)==True):
                res.append((i,i+2))
    print(res)
    return res
    
    
Twinprime(1,15)