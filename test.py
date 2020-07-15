a=[[1,2],[2,3]]
b=[[3,4],[5,6]]	

def n(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=a[i][j]+b[i][j]


# c=[[x+y for x,y in zip(c,d)]for c, d in zip(a,b)]

print(n(a,b))