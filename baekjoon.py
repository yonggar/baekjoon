M=int(input())
N=int(input())

d=[]
for i in range(M,N+1):
    if i==2:
        d.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                break
            elif i==j+1:
                d.append(i)

if d==[]:
    print(-1)
else:
    print(sum(d))
    print(d[0])
