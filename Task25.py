# Ericsson question
def solution(A):
    if len(A)%2 !=0:
        return False
    else:
        s= set(A)
        if len(s) == (len(A)/2):
            return True
        else:
            return False
#Test cases :)
print(solution([7,7,7]))
print(solution([1,2,2,1]))
print(solution([1,2,2,3]))


