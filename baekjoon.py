T=int(input())

while T!=0:
    T-=1
    k=int(input())
    n=int(input())
    X=[[] for _ in range(k+1)]
    X[0]=[i for i in range(n+1)]
    for i in range(1,k+1):
        a=[]
        for j in range(n+1):
            a.append(X[i][j]+X[i+1][j-1])
        X[i]=a

    print(X)

