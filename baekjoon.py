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
    M=[0,len(A),len(B),len(C)]
    # print(A)
    # print(B)
    # print(C)
    # print(M)

    if len(A)==len(B)==len(C):
        return [1,2,3]
    elif len(A)==len(B):
        if len(A)>len(C):
            return [1,2]
        else:
            return [3]
    elif len(B)==len(C):
        if len(B)>len(A):
            return [2,3]
        else:
            return [1]
    elif len(A)==len(C):
        if len(A)>len(B):
            return [1,3]
        else:
            return [2]
    else:
        return [M.index(max(M))]


print(mo([1,3,2,4,2,1,2,4,5,1,1,2,3,4,1,2,3,4]))

print(mo([1,2,3,4,5]))