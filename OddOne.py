def OddOne(L):
    P = {}
    for elem in L:
        if type(elem) not in P:
            P[type(elem)] = 0
        P[type(elem)] += 1
    for key, value in P.items():
        if value == 1:
            print(key.__name__)
            return key.__name__

OddOne([1.5,2.0,3.6,1,2.6,8.6])