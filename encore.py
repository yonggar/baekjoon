def solution(p,c):
    d={}
    for i in p:
        if i not in d: d[i]=1
        else: d[i]+=1
    print(d)

# def solution(participant, completion):
#     adict = dict() 
#     for elem in participant: 
#         if elem not in adict: adict[elem] = 1
#         else: adict[elem] += 1
#     print(adict)
    
#     for elem in completion: adict[elem] -= 1
#     for elem in adict: 
#         if adict[elem] != 0: return elem

participant=['mislav', 'stanko', 'mislav', 'ana']
completion=['stanko', 'ana', 'mislav']
print(solution(participant,completion))
