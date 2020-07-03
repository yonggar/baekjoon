import math
T=int(input())

while T!=0:
    T-=1
    x,y=map(int,input().split())
    s=y-x
    #s의 제곱근구하기
    sr=math.ceil(s**(1/2))
    #홀수수열값
    odd=2*sr-1
    if s**(1/2)==sr:
        print(odd)
    else:
        if s>sr**2-sr:
            print(odd)
        else:
            print(odd-1)

a=1
    ###s가 제곱근(1**2,2**2,3**2,4**2~)일때 (1,3,5,7,9~)수열을이룬다
    ###   제곱근 해당 수 만큼 처리과정이잇고 그앞은 -1
    ###cf) 49~56(14) 57~64(15) 65~72(16) 73~81(17) 82~90(18) 91~100(19)

    #제너레이터로만들어 메모리줄이기 or 마지막값으로만계산출력