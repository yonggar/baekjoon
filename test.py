def mo(m):
    len(m)
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,5]*2000
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    A=[]
    B=[]
    C=[]
    for i in range(len(m)):
        if m[i]==a[i]:
            A.append(i)
    for i in range(len(m)):
        if m[i]==b[i]:
            B.append(i)
    for i in range(len(m)):
        if m[i]==c[i]:
            C.append(i)
    M=[len(A),len(B),len(C)]
    return max(M)



print(mo([1,2,3,4,5]))
