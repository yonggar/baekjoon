# def prime(n):
#     if n==1:
#         return False
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         return True

M,N=map(int,input().split())

# for i in range(M,N+1):
#     if prime(i):
#         print(i)

for i in range(M,N+1):
    if i==1:
        continue
    if i==2:
        print(i)
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        print(i) 
