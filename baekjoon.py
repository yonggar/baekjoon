T=int(input())

while T!=0:
    T-=1
    k=int(input())
    n=int(input())
    X=[[] for _ in range(k+1)]
    X[0]=[i for i in range(n+1)]
    for i in range(1,k+1):
        X[i]=[0]
        for j in range(n):
            X[i].append(X[i-1][j+1]+X[i][j])

    print(X[k][n])

