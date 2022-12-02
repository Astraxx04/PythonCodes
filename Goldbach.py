def prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True

def Goldbach(a):
    res=[]
    for i in range((a//2)+1):
        if prime(i)==True:
            if prime(a-i)==True:
                res.append((i,a-i))
    print(res)
    return res

Goldbach(16)