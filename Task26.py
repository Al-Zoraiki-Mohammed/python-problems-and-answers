#Ericsson Question
def solution(A):
    l= [i for i in A]
    L=[]
    for i in range(len(l)):
        L.append(''.join(l[0:i]+l[i+1:])) 
    return min(L)

print(solution('codility'))



    
